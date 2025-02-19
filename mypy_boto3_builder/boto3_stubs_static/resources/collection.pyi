import logging
from typing import Any, Generic, Iterator, List, TypeVar

from boto3.resources.base import ServiceResource
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Collection
from boto3.resources.response import ResourceHandler
from boto3.utils import ServiceContext
from botocore.hooks import HierarchicalEmitter

logger: logging.Logger

_ResourceCollectionType = TypeVar("_ResourceCollectionType", bound="ResourceCollection[Any]")
_ServiceResourceType = TypeVar("_ServiceResourceType", bound="ServiceResource")

class ResourceCollection(Generic[_ServiceResourceType]):
    def __init__(
        self, model: Collection, parent: ServiceResource, handler: ResourceHandler, **kwargs: Any
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterator[Any]: ...
    def pages(self) -> Iterator[List[_ServiceResourceType]]: ...
    def all(self: _ResourceCollectionType) -> _ResourceCollectionType: ...
    def filter(self: _ResourceCollectionType, **kwargs: Any) -> _ResourceCollectionType: ...
    def limit(self: _ResourceCollectionType, count: int) -> _ResourceCollectionType: ...
    def page_size(self: _ResourceCollectionType, count: int) -> _ResourceCollectionType: ...

class CollectionManager(Generic[_ServiceResourceType]):
    _collection_cls = ResourceCollection[Any]
    def __init__(
        self,
        collection_model: Collection,
        parent: ServiceResource,
        factory: ResourceFactory,
        service_context: ServiceContext,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def iterator(self, **kwargs: Any) -> ResourceCollection[_ServiceResourceType]: ...
    def all(self) -> ResourceCollection[_ServiceResourceType]: ...
    def filter(self, **kwargs: Any) -> ResourceCollection[_ServiceResourceType]: ...
    def limit(self, count: int) -> ResourceCollection[_ServiceResourceType]: ...
    def page_size(self, count: InterruptedError) -> ResourceCollection[_ServiceResourceType]: ...
    def pages(self) -> List[ServiceResource]: ...

class CollectionFactory:
    def load_from_definition(
        self,
        resource_name: str,
        collection_model: Collection,
        service_context: ServiceContext,
        event_emitter: HierarchicalEmitter,
    ) -> CollectionManager[Any]: ...
