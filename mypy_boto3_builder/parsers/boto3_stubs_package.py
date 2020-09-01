"""
Parser that produces `structures.Boto3StubsPackage`.
"""
from typing import List

from boto3.session import Session
from botocore.config import Config

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


def parse_boto3_stubs_package(
    session: Session, service_names: List[ServiceName]
) -> Boto3StubsPackage:
    """
    Parse data for boto3_stubs package.

    Arguments:
        session -- boto3 session.
        service_names -- All available service names.

    Returns:
        Boto3StubsPackage structure.
    """
    result = Boto3StubsPackage(service_names=service_names)
    for service_name in result.service_names:
        result.service_packages.append(parse_fake_service_package(session, service_name))

    init_arguments = [
        Argument("region_name", Type.str, Type.none),
        Argument("api_version", Type.str, Type.none),
        Argument("use_ssl", Type.bool, Type.none),
        Argument("verify", TypeSubscript(Type.Union, [Type.bool, Type.str]), Type.none),
        Argument("endpoint_url", Type.str, Type.none),
        Argument("aws_access_key_id", Type.str, Type.none),
        Argument("aws_secret_access_key", Type.str, Type.none),
        Argument("aws_session_token", Type.str, Type.none),
        Argument("config", TypeClass(Config), Type.none),
    ]

    for service_package in result.service_packages:
        client_function = Function(
            name="client",
            decorators=[Type.overload],
            docstring="",
            arguments=[
                Argument("service_name", TypeLiteral(service_package.service_name.boto3_name)),
                *init_arguments,
            ],
            return_type=ExternalImport(
                source=ImportString(
                    service_package.service_name.module_name, ServiceModuleName.client.value
                ),
                name=service_package.client.name,
            ),
            body_lines=["..."],
        )
        result.init_functions.append(client_function)
        result.session_class.methods.append(
            Method(
                name="client",
                decorators=[Type.overload],
                docstring="",
                arguments=[
                    Argument("self", None),
                    Argument("service_name", TypeLiteral(service_package.service_name.boto3_name)),
                    *init_arguments,
                ],
                return_type=ExternalImport(
                    source=ImportString(
                        service_package.service_name.module_name, ServiceModuleName.client.value
                    ),
                    name=service_package.client.name,
                ),
                body_lines=["..."],
            )
        )

    for service_package in result.service_packages:
        if service_package.service_resource:
            client_function = Function(
                name="resource",
                decorators=[Type.overload],
                docstring="",
                arguments=[
                    Argument("service_name", TypeLiteral(service_package.service_name.boto3_name)),
                    *init_arguments,
                ],
                return_type=ExternalImport(
                    source=ImportString(
                        service_package.service_name.module_name,
                        ServiceModuleName.service_resource.value,
                    ),
                    name=service_package.service_resource.name,
                ),
                body_lines=["..."],
            )
            result.init_functions.append(client_function)
            result.session_class.methods.append(
                Method(
                    name="resource",
                    decorators=[Type.overload],
                    docstring="",
                    arguments=[
                        Argument("self", None),
                        Argument(
                            "service_name", TypeLiteral(service_package.service_name.boto3_name)
                        ),
                        *init_arguments,
                    ],
                    return_type=ExternalImport(
                        source=ImportString(
                            service_package.service_name.module_name,
                            ServiceModuleName.service_resource.value,
                        ),
                        name=service_package.service_resource.name,
                    ),
                    body_lines=["..."],
                )
            )

    return result
