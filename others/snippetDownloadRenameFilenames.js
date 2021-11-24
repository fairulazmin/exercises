//rename filename
const PREFIX = "1.";
const SOURCE = "youtube";

const download = () => {
    const list = document.getElementById("tbody").children;

    arr = [];
    renamedArr = [];

    for (let i = 0; i < list.length; i++) {
      arr.push(list[i].children[0].getAttribute("data-value"));
    }

    pattern = {
        downloadly: /.+\s[0]?(\d+\s[-]\s.+)/, 
        correction: /[1]\.(\d+\s[-]\s.+)/,
        youtube: /(.+)\s\(.+\)([.].+)/
    }


    arr.map((li) => {
      const fname = li.match(pattern[SOURCE]);
      fname && renamedArr.push(`mv "${li}" "${PREFIX}${fname[1]}${fname[2] || ''}"`);
      finalArr = renamedArr.join("\r\n");
    })

    //create blob
    blob = new Blob([finalArr], {type: "text/plain"})
    e = document.createEvent('MouseEvents')
    a = document.createElement('a')

    a.download = "filesRename.txt"
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}

download()
