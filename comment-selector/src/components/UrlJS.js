import React from 'react'
import snoowrap from 'snoowrap'
class UrlJS extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        data: null,
        value: 'https://www.reddit.com/r/AskReddit/comments/esr647/what_are_you_good_at_but_hate_doing/'
      };
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      // this.getRedditApi = this.getRedditApi.bind(this);
    }


    handleChange(event) {
        this.setState({value: event.target.value});
    }

    getRedditApi(){
      // alert(this.state.value);
      // Create a new snoowrap requester with OAuth credentials.
      // For more information on getting credentials, see here: https://github.com/not-an-aardvark/reddit-oauth-helper
      const r = new snoowrap({
        userAgent: 'gitpagesvideomaker',
        clientId: 'lFBsLCHPrHFysw',
        clientSecret: '21ykMnnDEFWTOUByvjRpZ_BKdZc',
        refreshToken: '204779307169-p6XxA40QkFisQyBpYu5YN_ks2Uk'
      });

      // Printing a list of the titles on the front page
      r.getHot().map(post => post.title).then(console.log);
      // Extracting every comment on a thread
      r.getSubmission('4j8p6d').expandReplies({limit: Infinity, depth: Infinity}).then(console.log)
    }
    // getRedditApi() {
    //     // alert(this.state.value);
    //     return fetch('http://127.0.0.1:5000/getdatajson', {
    //             method: 'POST',
    //             headers: {
    //                 Accept: 'application/json',
    //                 'Content-Type': 'application/json',
    //             },
    //             body: JSON.stringify({
    //                 url: this.state.value
    //             }),
    //         }).then((response) => response.json())
    //         .then((responseJson) => {
    //           return responseJson;
    //         })
    //         .catch((error) => {
    //           console.error(error);
    //         });
    // }
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

  export default UrlJS;