import logging as default_logging
from apache_beam.runners.interactive import interactive_environment as ie
from apache_beam.runners.interactive import interactive_beam as ib
from apache_beam.runners.interactive import interactive_runner as ir
from apache_beam.runners.interactive.caching import pipeline_cache as pc
from apache_beam.runners.interactive.caching import cacheable as c
from apache_beam.runners.interactive.caching import watermarks as wm
from apache_beam.runners.interactive.caching import background_caching_job as bcj
from apache_beam.runners.interactive.caching import cache_manager as cm
from apache_beam.runners.interactive.caching import cacheable as c
from apache_beam.runners.interactive.caching import watermarks as wm
from apache_beam.runners.interactive.caching import background_caching_job as bcj
from apache_beam.runners.interactive.caching import cache_manager as cm
from apache_beam.runners.interactive.caching import pipeline_cache as pc
from apache_beam.runners.interactive import interactive_environment as ie
from apache_beam.runners.interactive import interactive_beam as ib
from apache_beam.runners.interactive import interactive_runner as ir
from apache_beam.runners.interactive import interactive_runner_test_cache as irtc
from apache_beam.runners.interactive import interactive_runner_test_cache_manager as irtcm
from apache_beam.runners.interactive import interactive_runner_test_cacheable as irtc
from apache_beam.runners.interactive import interactive_runner_test_watermarks as irtw
from apache_beam.runners.interactive import interactive_runner_test_background_caching_job as irtbcj
from apache_beam.runners.interactive import interactive_runner_test_cache_manager as irtcm
from apache_beam.runners.interactive import interactive_runner_test_cacheable as irtc
from apache_beam.runners.interactive import interactive_runner_test_watermarks as irtw
from apache_beam.runners.interactive import interactive_environment_test as iet
from apache_beam.runners.interactive import interactive_beam_test as ibt
from backend.susy.main import SSQCD1, Bosonic, Fermionic


def main():
    # Set logging level, pipeline name, and pipeline root
    default_logging.basicConfig(level=default_logging.INFO)
    pipeline_name = "SSQC1"
    pipeline_root = "path/to/pipeline_root"

    # Initialize the Bosonic and Fermionic agents
    #    - Bosonic agent: responsible for the pipeline
    #      - Metadata connection
    #      - Interactive context
    #      - Components
    #       - Example gen
    #       - Statistics gen
    #       - Schema gen
    #       - Example validator
    #      - Adjust to the Fermionic agent's execution artifacts, observations, and state
    #
    #   - Fermionic agent: responsible for the data
    #      - Observe the Bosonic agent
    #      - Execute the pipeline
    #      - Adjust to the Bosonic agent's observations
    #    - Bosonic agent observes the Fermionic agent
    #    - Fermionic agent observes the Bosonic agent
    #    - These agents adjust to the other agent's observations towards alignment to the super-algebra of the system
    # Bosonic agent
    bosonic_agent = Bosonic(pipeline_name, pipeline_root)
    bosonic_agent.observe_supersymmetric("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_circuit("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_error_correction("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_qubit("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_state("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_algorithm("qubit_state")
    bosonic_agent.observe_supersymmetric_simulation_wolfram("qubit_state")
    bosonic_agent.observe_metadata("artifact")
    bosonic_agent.get_metadata_view("Any")

    # Fermionic agent
    fermionic_agent = Fermionic(pipeline_name, pipeline_root)
    fermionic_agent.observe_supersymmetric("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_circuit("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_error_correction("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_qubit("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_state("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_algorithm("qubit_state")
    fermionic_agent.observe_supersymmetric_simulation_wolfram("qubit_state")
    fermionic_agent.observe_metadata("artifact")
    fermionic_agent.get_metadata_view("Any")
    fermionic_agent.observe_state("qubit_state")
    fermionic_agent.observe_state_view("Any")

    # Bosonic agent observes the Fermionic agent
    bosonic_agent.observe_state(fermionic_agent.qubit_state)
    bosonic_agent.observe_state_view(fermionic_agent.state_view)

    # Fermionic agent observes the Bosonic agent
    fermionic_agent.observe_state(bosonic_agent.qubit_state)
    fermionic_agent.observe_state_view(bosonic_agent.state_view)

    # Instantiate the pipeline
    bosonic_pipeline = bosonic_agent.instantiate_pipeline()
    fermionic_pipeline = fermionic_agent.instantiate_pipeline()

    # Initialize the communication channel between the agents
    channel = SSQCD.Channel(
        bosonic_pipeline,
        fermionic_pipeline
    )

    # Initialize the pipeline
    pipeline = SSQCD1.Pipeline(
        channel=channel,
        bosonic_pipeline=bosonic_pipeline,
        fermionic_pipeline=fermionic_pipeline
    )

    # Execute the pipeline
    BeamDagRunner().run(pipeline)


if __name__ == "__main__":
    main()