    const list = document.getElementById("tbody").children;

    arr = [];
    renamedArr = [];

    for (let i = 0; i < list.length; i++) {
      arr.push(list[i].children[0].getAttribute("data-value"));
    }

    //rename filename
    const PREFIX = "2.";
    arr.map((li) => {
        
      //for original files
      const fname = li.match(/.+\s[0]?(\d+.+)/);
      fname && renamedArr.push(`ren "${li}" "${PREFIX}${fname[1]}"`);
      finalArr = renamedArr.join("\r\n");

      //for correction
      //const fname = li.match(/[1]\.(\d+.+)/);
      //console.log(`ren "${li}" "${PREFIX}${fname[1]}"`);
    })