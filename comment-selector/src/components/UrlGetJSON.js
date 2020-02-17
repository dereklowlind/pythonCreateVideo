import React from 'react'

class UrlGetJSON extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null,
        value: 'https://www.reddit.com/r/AskReddit/comments/esr647/what_are_you_good_at_but_hate_doing/'
      };
    //   this.handleFileSelect = this.handleFileSelect.bind(this);
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(event) {
        this.setState({value: event.target.value});
    }

    getRedditApi() {
      const url = 'http://127.0.0.1:5000/getdatajson';
      // const url = 'https://us-central1-pythonvideomaker.cloudfunctions.net/call-reddit-python';
    
        // alert(this.state.value);
        return fetch(url, {
                method: 'POST',
                //mode: 'no-cors',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: this.state.value
                }),
            }).then((response) => response.json())
            .then((responseJson) => {
              return responseJson;
            })
            .catch((error) => {
              console.error(error);
            });
    }
    handleSubmit(event) {
        this.getRedditApi()
        .then((responseJson) => {
            this.setState({data: responseJson});
            this.props.parentCallback(responseJson);
        });

        event.preventDefault();
    }
  
    render() {
      return (
        <div>
            <form onSubmit={this.handleSubmit}>
                <label>
                    URL:
                    <input type="text" 
                        value={this.state.value} 
                        onChange={this.handleChange}
                    />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </div>
      );
    }
  }

  export default UrlGetJSON;