_CONFIG = dict(
    _METADATA_TYPES=dict(
        _METADATA_TYPES_ENUM=(
            artifact="",
            data="",
            data_type="",
            data_shape="",
            data_dtype="",
            data_size="",
            data_ndim="",
            data_nbytes="",
            data_T="",
            data_real="",
            data_imag="",
            data_flat="",
            data_imag_flat="",
            data_real_flat="",
            data_min="",
            data_max="",
            data_argmin="",
            data_argmax="",
            data_sum="",
            data_prod="",
            data_mean="",
            data_std="",
            data_var="",
            data_all="",
            data_any="",
            data_cumsum="",
            data_cumprod="",
            data_trace="",
            data_transpose="",
            data_conj="",
            data_round="",
            data_array_equal="",
            data_array_equiv="",
            data_array_repr="",
            data_array_str="",
            data_compress="",
            data_copy="",
            data_cumulative_product="",
            data_cumulative_sum="",
            data_diagonal="",
            data_dot="",
            data_fill_diagonal="",
            data_flatten="",
            data_getfield="",
            data_item="",
            data_itemset="",
            data_newbyteorder="",
            data_partition="",
            data_put="",
            data_ravel="",
            data_repeat="",
            data_reshape="",
            data_resize="",
            data_squeeze="",
            data_swapaxes="",
            data_take="",
            data_tobytes="",
            data_tofile="",
            data_tolist="",
            data_tostring="",
            data_view="",
            data_argpartition="",
            data_argsort="",
            data_choose="",
            data_clip=""
        )
    ),
    _PIPELINE_COMPONENTS=dict(
        CsvExampleGen=CsvExampleGen,
        StatisticsGen=StatisticsGen,
        SchemaGen=SchemaGen,
        ExampleValidator=ExampleValidator,
        Transform=Transform,
        Trainer=Trainer,
        Pusher=Pusher,
        BulkInferrer=BulkInferrer
    ),
    _PIPELINE_COMPONENTS_ENUM=dict(
        "CsvExampleGen",
        "StatisticsGen",
        "SchemaGen",
        "ExampleValidator",
        "Transform",
        "Trainer",
        "Pusher",
        "BulkInferrer"
    ),
    _PIPELINE_COMPONENTS_SPEC=dict(
        CsvExampleGen=ComponentSpec.,
        StatisticsGen=StatisticsGenSpec,
        SchemaGen=SchemaGenSpec,
        ExampleValidator=ExampleValidatorSpec,
        Transform=TransformSpec,
        Trainer=TrainerSpec,
        Pusher=PusherSpec,
        BulkInferrer=BulkInferrerSpec
    ),
    _PIPELINE_COMPONENTS_SPEC_ENUM=(
        "CsvExampleGenSpec",
        "StatisticsGenSpec",
        "SchemaGenSpec",
        "ExampleValidatorSpec",
        "TransformSpec",
        "TrainerSpec",
        "PusherSpec",
        "BulkInferrerSpec"
    ),
    _PIPELINE_COMPONENTS_SPEC_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_SPEC_CHANNEL_ENUM=(
        CsvExampleGen="Channel",
        StatisticsGen="Channel",
        SchemaGen="Channel",
        ExampleValidator="Channel",
        Transform="Channel",
        Trainer="Channel",
        Pusher="Channel",
        BulkInferrer="Channel"
    ),
    _PIPELINE_COMPONENTS_SPEC_CHANNEL_TYPE=dict(
        CsvExampleGen=Artifact,
        StatisticsGen=Artifact,
        SchemaGen=Artifact,
        ExampleValidator=Artifact,
        Transform=Artifact,
        Trainer=Artifact,
        Pusher=Artifact,
        BulkInferrer=Artifact
    ),
    _PIPELINE_COMPONENTS_SPEC_CHANNEL_TYPE_ENUM=(
        CsvExampleGen="Artifact",
        StatisticsGen="Artifact",
        SchemaGen="Artifact",
        ExampleValidator="Artifact",
        Transform="Artifact",
        Trainer="Artifact",
        Pusher="Artifact",
        BulkInferrer="Artifact"
    ),
    _PIPELINE_COMPONENTS_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_OUTPUT=dict(
        CsvExampleGen=Artifact,
        StatisticsGen=Artifact,
        SchemaGen=Artifact,
        ExampleValidator=Artifact,
        Transform=Artifact,
        Trainer=Artifact,
        Pusher=Artifact,
        BulkInferrer=Artifact
    ),
    _PIPELINE_COMPONENTS_INPUT=dict(
        CsvExampleGen=Artifact,
        StatisticsGen=Artifact,
        SchemaGen=Artifact,
        ExampleValidator=Artifact,
        Transform=Artifact,
        Trainer=Artifact,
        Pusher=Artifact,
        BulkInferrer=Artifact
    ),
    _PIPELINE_COMPONENTS_OUTPUT_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_INPUT_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_OUTPUT_SPEC=dict(
        CsvExampleGen=tfx.types.standard_artifacts.Examples,
        StatisticsGen=tfx.types.standard_artifacts.ExampleStatistics,
        SchemaGen=tfx.types.standard_artifacts.Schema,
        ExampleValidator=tfx.types.standard_artifacts.ExampleAnomalies,
        Transform=tfx.types.standard_artifacts.TransformGraph,
        Trainer=tfx.types.standard_artifacts.Model,
        Pusher=tfx.types.standard_artifacts.PushedModel,
        BulkInferrer=tfx.types.standard_artifacts.InferenceResult
    ),
    _PIPELINE_COMPONENTS_INPUT_SPEC=dict(
        CsvExampleGen=tfx.types.standard_artifacts.Examples,
        StatisticsGen=tfx.types.standard_artifacts.ExampleStatistics,
        SchemaGen=tfx.types.standard_artifacts.Schema,
        ExampleValidator=tfx.types.standard_artifacts.ExampleAnomalies,
        Transform=tfx.types.standard_artifacts.TransformGraph,
        Trainer=tfx.types.standard_artifacts.Model,
        Pusher=tfx.types.standard_artifacts.PushedModel,
        BulkInferrer=tfx.types.standard_artifacts.InferenceResult
    ),
    _PIPELINE_COMPONENTS_OUTPUT_SPEC_TYPE=dict(
        CsvExampleGen=tfx.types.standard_artifacts.Examples,
        StatisticsGen=tfx.types.standard_artifacts.ExampleStatistics,
        SchemaGen=tfx.types.standard_artifacts.Schema,
        ExampleValidator=tfx.types.standard_artifacts.ExampleAnomalies,
        Transform=tfx.types.standard_artifacts.TransformGraph,
        Trainer=tfx.types.standard_artifacts.Model,
        Pusher=tfx.types.standard_artifacts.PushedModel,
        BulkInferrer=tfx.types.standard_artifacts.InferenceResult
    ),
    _PIPELINE_COMPONENTS_INPUT_SPEC_TYPE=dict(
        CsvExampleGen=tfx.types.standard_artifacts.Examples,
        StatisticsGen=tfx.types.standard_artifacts.ExampleStatistics,
        SchemaGen=tfx.types.standard_artifacts.Schema,
        ExampleValidator=tfx.types.standard_artifacts.ExampleAnomalies,
        Transform=tfx.types.standard_artifacts.TransformGraph,
        Trainer=tfx.types.standard_artifacts.Model,
        Pusher=tfx.types.standard_artifacts.PushedModel,
        BulkInferrer=tfx.types.standard_artifacts.InferenceResult
    ),
    _PIPELINE_COMPONENTS_OUTPUT_SPEC_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_INPUT_SPEC_CHANNEL=dict(
        CsvExampleGen=Channel,
        StatisticsGen=Channel,
        SchemaGen=Channel,
        ExampleValidator=Channel,
        Transform=Channel,
        Trainer=Channel,
        Pusher=Channel,
        BulkInferrer=Channel
    ),
    _PIPELINE_COMPONENTS_OUTPUT_SPEC_CHANNEL_TYPE=dict(
        CsvExampleGen="Channel",
        StatisticsGen="Channel",
        SchemaGen="Channel",
        ExampleValidator="Channel",
        Transform="Channel",
        Trainer="Channel",
        Pusher="Channel",
        BulkInferrer="Channel"
    ),
    _PIPELINE_COMPONENTS_INPUT_SPEC_CHANNEL_TYPE=dict(
        CsvExampleGen="Channel",
        StatisticsGen="Channel",
        SchemaGen="Channel",
        ExampleValidator="Channel",
        Transform="Channel",
        Trainer="Channel",
        Pusher="Channel",
        BulkInferrer="Channel"
    ),
    _PIPELINE_COMPONENTS_OUTPUT_SPEC_TYPE_CHANNEL=dict(
        CsvExampleGen="Channel",
        StatisticsGen="Channel",
        SchemaGen="Channel",
        ExampleValidator="Channel",
        Transform="Channel",
        Trainer="Channel",
        Pusher="Channel",
        BulkInferrer="Channel"
    ),
    _PIPELINE_COMPONENTS_INPUT_SPEC_TYPE_CHANNEL=dict(
        CsvExampleGen="Channel",
        StatisticsGen="Channel",
        SchemaGen="Channel",
        ExampleValidator="Channel",
        Transform="Channel",
        Trainer="Channel",
        Pusher="Channel",
        BulkInferrer="Channel"
    )
)

class SSQCPipelineConfig(PipelineConfig):
    """
    SuperSymmetric Quantum Computer Pipeline Configuration
    """

    def __init__(self, **kwargs):
        super(SSQCPipelineConfig, self).__init__(**kwargs)
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self._logger.info("Initializing SSQC Pipeline Configuration...")
        self._logger.info("Initializing SSQC Pipeline Components...")
        self._components = _PIPELINE_COMPONENTS
        self._logger.info("Initializing SSQC Pipeline Components Spec...")
        self._components_spec = _PIPELINE_COMPONENTS_SPEC
        self._logger.info("Initializing SSQC Pipeline Components Channel...")
        self._components_channel = _PIPELINE_COMPONENTS_CHANNEL
        self._logger.info("Initializing SSQC Pipeline Components Output...")
        self._components_output = _PIPELINE_COMPONENTS_OUTPUT
        self._logger.info("Initializing SSQC Pipeline Components Input...")
        self._components_input = _PIPELINE_COMPONENTS_INPUT
        self._logger.info("Initializing SSQC Pipeline Components Output Channel...")
        self._components_output_channel = _PIPELINE_COMPONENTS_OUTPUT_CHANNEL
        self._logger.info("Initializing SSQC Pipeline Components Input Channel...")
        self._components_input_channel = _PIPELINE_COMPONENTS_INPUT_CHANNEL
        self._logger.info("Initializing SSQC Pipeline Components Output Spec...")
        self._components_output_spec = _PIPELINE_COMPONENTS_OUTPUT_SPEC
        self._logger.info("Initializing SSQC Pipeline Components Input Spec...")
        self._components_input_spec = _PIPELINE_COMPONENTS_INPUT_SPEC
        self._logger.info("Initializing SSQC Pipeline Components Output Spec Type...")
        self._components_output_spec_type = _PIPELINE_COMPONENTS_OUTPUT_SPEC_TYPE
        self._logger.info("Initializing SSQC Pipeline Components Input Spec Type...")
        self._components_input_spec_type = _PIPELINE_COMPONENTS_INPUT_SPEC_TYPE

    @property
    def components(self):
        return self._components

    @property
    def components_spec(self):
        return self._components_spec

    @property
    def components_channel(self):
        return self._components_channel

    @property
    def components_output(self):
        return self._components_output

    @property
    def components_input(self):
        return self._components_input

    @property
    def components_output_channel(self):
        return self._components_output_channel

    @property
    def components_input_channel(self):
        return self._components_input_channel

    @property
    def components_output_spec(self):
        return self._components_output_spec

    @property
    def components_input_spec(self):
        return self._components_input_spec

    @property
    def components_output_spec_type(self):
        return self._components_output_spec_type

    @property
    def components_input_spec_type(self):
        return self._components_input_spec_type

