import builtins
import difflib
import sys

def reminder_mocker(start, path):
    
    text = ""
    expected_lines = _parse_expected_lines(path)
    responses = _extract_responses(expected_lines)
    
    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
        
    def mock_input(*args):
        nonlocal text
        if not len(responses):
            sys.exit()
        response = responses.pop(0)
        text += "".join(args) + response + "\n"
        return response
    
    real_print = builtins.print
    real_input = builtins.input
    
    builtins.print = mock_print
    builtins.input = mock_input
    
    try:
        start()
    except SystemExit:
        real_print("No problem. System exits are allowed in this app.")
        
    builtins.print = real_print
    builtins.input = real_input

    return _find_differences(text, expected_lines)


def _parse_expected_lines(path):
    with open(path) as f:
            expected_lines = f.read().splitlines()
    return expected_lines

def _extract_responses(lines):
    responses = []
    for line in lines:
        if line.startswith("➤"):
            response = line.replace("➤➤➤   ", "").strip()
            responses.append(response)
    return responses

def _find_differences(text, expected_lines):
    actual_lines = text.splitlines()
    diffed = difflib.unified_diff(actual_lines, expected_lines, lineterm="")
    return "\n".join(diffed)