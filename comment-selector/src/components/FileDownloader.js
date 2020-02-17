import React from 'react'

class FileDownloader extends React.Component {
  downloadTxtFile = () => {
    const element = document.createElement("a");
    const file = new Blob([JSON.stringify(this.props.data)], {type: 'application/json'});
    element.href = URL.createObjectURL(file);
    element.download = this.props.data.id + ".json";
    document.body.appendChild(element); // Required for this to work in FireFox
    element.click();
  }
  
    render() {
      return (
        <div>
        <a>Download JSON File </a>
        <button onClick={this.downloadTxtFile}>Download txt</button>
        </div>
      );
    }
  }

  export default FileDownloader;