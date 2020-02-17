import React from 'react'

class FileSelector extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null
      };
      this.handleFileSelect = this.handleFileSelect.bind(this);
    }
    displayData(content) {
      this.setState({data: content});
    }
  
    handleFileSelect(evt) {
      let files = evt.target.files;
      if (!files.length) {
        alert('No file select');
        return;
      }
      let file = files[0];
      let that = this;
      let reader = new FileReader();
      reader.onload = function(e) {
        that.displayData(e.target.result);
        that.props.parentCallback(JSON.parse(e.target.result));
      };
      reader.readAsText(file);
      
    
    }
  
    render() {
      return (
        <div>
        <a>Select JSON File </a>
          <input type="file" onChange={this.handleFileSelect}/>
          {/* { data && <p> {data} </p> } */}
        </div>
      );
    }
  }

  export default FileSelector;