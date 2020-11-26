const runner = new BrythonRunner({
    stdout: {
        write(content) {
            // Show output messages here.
            output.setValue(output.getValue()+content)
            console.log('StdOut: ' + content);
        },
        flush() {
          //document.getElementById('output').value = ''
        },
    },
    stderr: {
        write(content) {
            // Show error messages here.
            output.setValue(output.getValue()+content)
        },
        flush() {},
    },
    stdin: {
        async readline() {
            var userInput = prompt();
            console.log('Received StdIn: ' + userInput);
            return userInput;
        },
    }
});
async function custom_run() {
  output.setValue('Программа запускается...\n')
  text = editor.getValue()
  await runner.runCode(text)
}
