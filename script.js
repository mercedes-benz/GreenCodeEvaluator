let input = document.querySelector('input');
let textarea = document.querySelector('textarea');
var colors = [];
input.addEventListener('change', () => {
  let files = input.files;
  if (files.length == 0) return;
  const file = files[0];
  let reader = new FileReader();
  reader.onload = (e) => {
    const file = e.target.result;
    const lines = file.split(/\r\n|\n/);
    textarea.value = lines.join('\n');

    const selectorExp = /\s*([^{]+?)\s*\{\s*([^}]+?)\s*\}/g;
    const colorExp = /(^|[\s;])color\s*:\s*([^;]+)/i;

    let selectorMatch;

    while (selectorMatch = selectorExp.exec(lines)) {
      const [match, selectors, rules] = selectorMatch;
      const colorMatch = colorExp.exec(rules);

      if (colorMatch) {
        colors = colors.concat(selectors.split(/\s*,\s*/g).map(s => ({
         // selector: s,
          color: colorMatch[2]
        })));
      }
    }

    textarea.value += colors.toString();
      console.log(colors.toString());

  };
  reader.onerror = (e) => alert(e.target.error.name);
  reader.readAsText(file);


});
