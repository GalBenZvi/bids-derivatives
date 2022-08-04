#: SingleSubjectDerivatives messages

PARTICIPANT_MISMATCH = "Participant label {participant_label} does not match the base directory name {base_dir_name}!"

PARTICIPANT_MISSING = (
    "Participant {participant_label} does not exist in {base_directory}"
)

PARTICIPANT_COULD_NOT_BE_DETERMINED = "Participant label not specified and could not be determined by the base directory name."

INVALID_ROOT = """The root directory of the derivatives' dataset must either contain a 'derivatives' directory comprised of BIDS-Apps' outputs,
or be the root of a BIDS-App's output iself."""
