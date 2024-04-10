import code
import sys
import io


class CapturingInterpreter(code.InteractiveInterpreter):
    def __init__(self, locals=None):
        super().__init__(locals=locals)
        self.output_buffer = io.StringIO()

    def runsource(self, source, filename='<input>', symbol='single'):
        # Redirect stdout to our buffer
        original_stdout = sys.stdout
        sys.stdout = self.output_buffer
        try:
            # Now, run the source code
            super().runsource(source, filename, symbol)
        finally:
            # Ensure stdout is restored
            sys.stdout = original_stdout

    def get_output(self):
        # Retrieve the captured output and clear the buffer for next use
        output = self.output_buffer.getvalue()
        self.output_buffer.truncate(0)
        self.output_buffer.seek(0)
        return output
