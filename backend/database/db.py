class ArtifactStore(mlmd.metadata_store.MetadataStore, SusyQuantumRegister):
    Type = Type[mlmd.metadata_store.MetadataStore]
    Config = Dict[mlmd_proto.MetadataStoreClientConfig]
    default_kwargs = dict(
        type=Type,
        config=Config,
        _store={},
        _type='sqlite',
        _host='localhost',
        _port=3306,
        _database='metadata'
    )
    MetadataStore = mlmd.metadata_store.MetadataStore(**default_kwargs)

    def __init__(self, kwargs: Dict[str, Any] = None):
        super().__init__(self, **kwargs)
        self.uri = uri_template.URITemplate(template="{_type}://{_host}:{_port}/{_database}")
        self.store = self.MetadataStore
        self._store = dict(
            ids=[artifact.id for artifact in self.store.get_artifacts()],
            types=[artifact.type for artifact in self.store.get_artifacts()],
            properties=[artifact.properties for artifact in self.store.get_artifacts()],
            custom_properties=[artifact.custom_properties for artifact in self.store.get_artifacts()],
            state=[artifact.state for artifact in self.store.get_artifacts()],
            create_time_since_epoch=[artifact.create_time_since_epoch for artifact in self.store.get_artifacts()],
            last_update_time_since_epoch=[artifact.last_update_time_since_epoch for artifact in
                                          self.store.get_artifacts()],
            type_id=[artifact.type_id for artifact in self.store.get_artifacts()],
            uri=[artifact.uri for artifact in self.store.get_artifacts()],
            name=[artifact.name for artifact in self.store.get_artifacts()],
            version=[artifact.version for artifact in self.store.get_artifacts()],
            description=[artifact.description for artifact in self.store.get_artifacts()],
        )

        for k, v in self.default_kwargs.items():
            self.__setattr__(k, v)

    def get_artifact(self, artifact_id: int) -> Any:
        return self._store[artifact_id]

    def put_artifact(self, artifact: Any) -> int:
        artifact_id = len(self._store)
        self._store[artifact_id] = artifact
        return artifact_id

    def get_artifacts_by_type(self, type_name: str, type_version: Optional[str] = None, artifact_type=None) -> list:
        return [artifact for artifact in self._store.values() if artifact.type == artifact_type]

    def get_artifacts_by_uri(self, uri: str, artifact_type=None) -> list[Any]:
        return [artifact for artifact in self._store.values() if artifact.type == artifact_type and artifact.uri == uri]

    def get_artifacts_by_property(self, artifact_type: str, property_name: str, property_value: Any) -> list[Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.properties[property_name] == property_value]

    def get_artifacts_by_properties(self, artifact_type: str, properties: dict[str, Any]) -> list[Any]:
        return [artifact for artifact in self._store.values() if artifact.type == artifact_type and all(
            artifact.properties[property_name] == property_value for property_name, property_value in properties.items()
        )]

    def get_artifacts_by_type_and_property(self, artifact_type: str, property_name: str, property_value: Any) -> list[
        Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.properties[property_name] == property_value]

    def get_artifacts_by_type_and_properties(self, artifact_type: str, properties: dict[str, Any]) -> list[Any]:
        return [artifact for artifact in self._store.values() if artifact.type == artifact_type and all(
            artifact.properties[property_name] == property_value for property_name, property_value in properties.items()
        )]

    def get_artifacts_by_uri_and_property(
        self,
        artifact_type: str,
        uri: str,
        property_name: str,
        property_value: Any
    ) -> list[Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and artifact.properties[
                    property_name] == property_value]

    def get_artifacts_by_uri_and_properties(self, artifact_type: str, uri: str, properties: dict[str, Any]) -> list[
        Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )]

    def get_artifacts_by_type_and_uri_and_property(
        self,
        artifact_type: str,
        uri: str,
        property_name: str,
        property_value: Any
    ) -> list[Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and artifact.properties[
                    property_name] == property_value]

    def get_artifacts_by_type_and_uri_and_properties(self, artifact_type: str, uri: str, properties: dict[str,
    Any]) -> \
    list[Any]:
        return [artifact for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )]

    def put_artifacts(self, artifacts: list[Any]) -> list[int]:
        return [self.put_artifact(artifact) for artifact in artifacts]

    def get_artifact_types(self) -> list[str]:
        return list(set(artifact.type for artifact in self._store.values()))

    def get_artifact_properties(self, artifact_type: str) -> list[str]:
        return list(
            set(
                property_name for artifact in self._store.values() if artifact.type == artifact_type for property_name
                in artifact.properties.keys()
            )
        )

    def get_artifact_property_values(self, artifact_type: str, property_name: str) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type
            )
        )

    def get_artifact_property_values_by_uri(self, artifact_type: str, uri: str, property_name: str) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri
            )
        )

    def get_artifact_property_values_by_properties(
        self,
        artifact_type: str,
        properties: dict[str, Any],
        property_name: str
    ) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )
            )
        )

    def get_artifact_property_values_by_uri_and_property(self, artifact_type: str, uri: str, property_name: str) -> \
    list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri
            )
        )

    def get_artifact_property_values_by_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any],
        property_name: str
    ) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )
            )
        )

    def get_artifact_property_values_by_type_and_property(self, artifact_type: str, property_name: str) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type
            )
        )

    def get_artifact_property_values_by_type_and_properties(
        self,
        artifact_type: str,
        properties: dict[str, Any],
        property_name: str
    ) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )
            )
        )

    def get_artifact_property_values_by_type_and_uri_and_property(
        self,
        artifact_type: str,
        uri: str,
        property_name: str
    ) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri
            )
        )

    def get_artifact_property_values_by_type_and_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any],
        property_name: str
    ) -> list[Any]:
        return list(
            set(
                artifact.properties[property_name] for artifact in self._store.values() if
                artifact.type == artifact_type and artifact.uri == uri and all(
                    artifact.properties[property_name] == property_value for property_name, property_value in
                    properties.items()
                )
            )
        )

    def visualize_artifacts(self, artifact_type: str, property_name: str, property_value: Any) -> None:
        artifacts = self.get_artifacts_by_type_and_property(artifact_type, property_name, property_value)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_uri(self, artifact_type: str, uri: str, property_name: str, property_value: Any) -> None:
        artifacts = self.get_artifacts_by_type_and_uri_and_property(artifact_type, uri, property_name, property_value)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_properties(self, artifact_type: str, properties: dict[str, Any]) -> None:
        artifacts = self.get_artifacts_by_type_and_properties(artifact_type, properties)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any],
        property_value: Any
    ) -> None:
        artifacts = self.get_artifacts_by_type_and_uri_and_properties(artifact_type, uri, properties)
        visualizations = []

        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")
            if artifact.properties.type == property_value:
                visualizations.append(artifact)

    def visualize_artifacts_by_type_and_property(
        self,
        artifact_type: str,
        property_name: str,
        property_value: Any
    ) -> None:
        artifacts = self.get_artifacts_by_type_and_property(artifact_type, property_name, property_value)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_type_and_uri(
        self,
        artifact_type: str,
        uri: str,
        property_name: str,
        property_value: Any
    ) -> None:
        artifacts = self.get_artifacts_by_type_and_uri_and_property(artifact_type, uri, property_name, property_value)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_type_and_properties(self, artifact_type: str, properties: dict[str, Any]) -> None:
        artifacts = self.get_artifacts_by_type_and_properties(artifact_type, properties)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifacts_by_type_and_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any]
    ) -> None:
        artifacts = self.get_artifacts_by_type_and_uri_and_properties(artifact_type, uri, properties)
        for artifact in artifacts:
            print(f"{artifact.uri}: {artifact.properties}")

    def visualize_artifact_property_values(self, artifact_type: str, property_name: str) -> None:
        values = self.get_artifact_property_values_by_type_and_property(artifact_type, property_name)
        print(values)

    def visualize_artifact_property_values_by_uri(self, artifact_type: str, uri: str, property_name: str) -> None:
        values = self.get_artifact_property_values_by_type_and_uri_and_property(artifact_type, uri, property_name)
        print(values)

    def visualize_artifact_property_values_by_properties(
        self,
        artifact_type: str,
        properties: dict[str, Any],
        property_name: str
    ) -> None:
        values = self.get_artifact_property_values_by_type_and_properties(artifact_type, properties, property_name)
        print(values)

    def visualize_artifact_property_values_by_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any],
        property_name: str
    ) -> None:
        values = self.get_artifact_property_values_by_type_and_uri_and_properties(
            artifact_type,
            uri,
            properties,
            property_name
        )
        print(values)

    def visualize_artifact_property_values_by_type_and_property(self, artifact_type: str, property_name: str) -> None:
        values = self.get_artifact_property_values_by_type_and_property(artifact_type, property_name)
        print(values)

    def visualize_artifact_property_values_by_type_and_uri(
        self,
        artifact_type: str,
        uri: str,
        property_name: str
    ) -> None:
        values = self.get_artifact_property_values_by_type_and_uri_and_property(artifact_type, uri, property_name)
        print(values)

    def visualize_artifact_property_values_by_type_and_properties(
        self,
        artifact_type: str,
        properties: dict[str, Any],
        property_name: str
    ) -> None:
        values = self.get_artifact_property_values_by_type_and_properties(artifact_type, properties, property_name)
        print(values)

    def visualize_artifact_property_values_by_type_and_uri_and_properties(
        self,
        artifact_type: str,
        uri: str,
        properties: dict[str, Any],
        property_name: str
    ) -> None:
        values = self.get_artifact_property_values_by_type_and_uri_and_properties(
            artifact_type,
            uri,
            properties,
            property_name
        )
        print(values)

    def __repr__(self, artifact_type=None, property_name=None) -> str:
        return f"ArtifactStore(artifact_type={artifact_type}, property_name={property_name})"

    def __str__(self, artifact_type=None, property_name=None) -> str:
        return f"ArtifactStore(artifact_type={artifact_type}, property_name={property_name})"

    def __eq__(self, other: Any) -> bool:
        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        return self.__dict__ != other.__dict__

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))

    def __getstate__(self) -> dict[str, Any]:
        return self.__dict__

        # TODO: Add support for pickling an artifact store

    def store_pickle(self, artifact_type: str, uri: str, properties: Union[str, Any], pickle: Any) -> None:
        pickled_artifact = PickledArtifact(artifact_type, uri, properties, pickle)
        self.store_artifact(pickled_artifact)

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__ = state

        # TODO: Add support for other artifact types

    def get_artifact_type(self, **kwargs) -> mlmd_proto.ArtifactType:
        return self.store.get_artifact_type(kwargs.get("artifact_type_name"))

        # TODO: Add support for initializing a view

    def get_view(self):
        return ArtifactStoreView(self)

        # TODO: Add support for storing transformations in a quantum bit register

    def store_transformation(self, transformation: Transformation) -> None:
        pass

        # TODO: Add support for storing pipelines in a quantum bit register

    def store_pipeline(
        self,
        pipeline: Union[apache_beam.Pipeline, tfx.dsl.Pipeline, Fermionic, Bosonic, QuantumPipeline, Any],
        options: Optional[Union[PipelineOptions, dict[str, Any]]] = None,
        pipeline_name: Optional[str] = None,
        pipeline_description: Optional[str] = None,
    ) -> Any:
        graph = {
            "pipeline": pipeline,
            "options": options,
            "pipeline_name": pipeline_name,
            "pipeline_description": pipeline_description,
        }
        self.store_artifact(PipelineGraphArtifact(**graph))

        # TODO: Add support for storing quantum circuits in a quantum bit register

    def store_quantum_circuit(self, quantum_circuit: QuantumCircuit) -> None:
        pass

        # TODO: Add support for storing quantum programs in a quantum bit register

    def store_quantum_program(self, quantum_program: QuantumProgram) -> None:
        pass

        # TODO: Add support for storing quantum algorithms in a quantum bit register

    def store_quantum_algorithm(self, quantum_algorithm: QuantumAlgorithm) -> None:
        pass

        # TODO: Add support for storing quantum models in a quantum bit register

    def store_quantum_model(self, quantum_model: QuantumModel) -> None:
        pass

        # TODO: Add support for storing quantum datasets in a quantum bit register

    def store_quantum_dataset(self, quantum_dataset: QuantumDataset) -> None:
        pass

        # TODO: Add support for storing representations in a quantum bit register

    def store_representation(self, representation: Representation) -> None:
        pass

        # TODO: Add support for storing quantum representations in a quantum bit register

    def store_quantum_representation(self, quantum_representation: QuantumRepresentation) -> None:
        pass

        # TODO: Add support for storing supersymmetric representations in a quantum bit register

    def store_supersymmetric_representation(self, supersymmetric_representation: SupersymmetricRepresentation) -> None:
        pass

        # TODO: Add support for storing generator representations in a quantum bit register

    def store_generator_representation(self, generator_representation: GeneratorRepresentation) -> None:
        pass

        # TODO: Add support for storing quantum generator functions in a quantum bit register

    def store_quantum_generator_function(self, quantum_generator_function: QuantumGeneratorFunction) -> None:
        pass

        # TODO: Add support for storing transformation groups and their corresponding algebras in a quantum bit register

    def store_transformation_group(self, transformation_group: TransformationGroup) -> None:
        pass

        # TODO: Add support for storing transformation group representations in a quantum bit register

    def store_transformation_group_representation(
        self,
        transformation_group_representation: TransformationGroupRepresentation
    ) -> None:
        pass

        # TODO: Add support for storing relationships and compositions of transformation group representations in a
        #  quantum bit register

    def store_transformation_group_representation_relationship(
        self,
        transformation_group_representation_relationship: TransformationGroupRepresentationRelationship
    ) -> None:
        pass

    def get_all_artifacts_types(self, artifact):
        return self.get_all_artifacts_types(artifact)

    def get_all_artifacts_of_type(self, artifact):
        return self.get_all_artifacts_of_type(artifact)

    def get_all_artifacts_of_type_by_type(self, artifact):
        return self.get_all_artifacts_of_type_by_type(artifact)

    def get_all_artifacts(self, artifact):
        return self.get_all_artifacts(artifact)

    def store_artifact(self, pickled_artifact):
        return self.store_artifact(pickled_artifact)

    def get_all_artifacts_of_type_by_type_by_type(self, artifact):
        pass
    
    
class PipelineGraphArtifact(mlmd_proto.Artifact, networkx.classes.MultiDiGraph):
    def __init__(self, name: str, uri: str, artifact_type: Any, metadata: Any):
        super().__init__()
        self.name = name
        self.uri = uri
        self.artifact_type = artifact_type
        self.metadata = metadata
        self.store = ArtifactStore(metadata.get('connection_config'))

    @wraps(Artifact.setter)
    def artifact_type(self) -> Union[str, mlmd_proto.ArtifactType]:
        return self.artifact_type

    def get_artifact(self, artifact_id: int) -> Any:
        return self.store.get_artifact(artifact_id)

    def put_artifact(self, artifact: Any) -> int:
        return self.store.put_artifact(artifact)

    def get_artifacts_by_type(self, type_name: str, type_version: Optional[str] = None, artifact_type=None) -> list:
        return self.store.get_artifacts_by_type(type_name, type_version, artifact_type)

    def get_artifacts_by_uri(self, uri: str) -> list:
        return self.store.get_artifacts_by_uri(uri)

    def get_artifacts_by_property(self, key: str, value: str) -> list:
        return self.store.get_artifacts_by_property(key, value)

    # TODO: Add more methods to the PipelineGraphArtifact class.
    #   - TODO: Add a method to get the artifact type.
    #   - TODO: Add a method to get the artifact metadata.
    #   - TODO: Add a method to get the artifact store.
    #
