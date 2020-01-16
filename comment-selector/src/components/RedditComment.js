import React from 'react'

class RedditComment extends React.Component {
    
    render(){
        let json = JSON.parse(this.props.data)
        // if(json == null){json=""}
        // const comment1 = json["commentData"][0]
        const comAuthorstyle = {
            fontsize: '12px',
            fontweight: '400',
            lineheight: '16px',
            color: '#0079D3'
        };
        const subAuthorstyle = {
            fontsize: '12px',
            fontweight: '400',
            lineheight: '16px',
            color: '#6c6e70'
        };

        const paragraphstyle = {
            fontfamily: 'Noto Sans,Arial,sans-serif',
            fontsize: '14px',
            fontweight: '400',
            lineheight: '21px',
            wordbreak: 'breakword',
            overflow: 'auto',
            paddingbottom: '1px',
            marginbottom: -'1px',
            color:'#1A1A1B'
        };
        if(json == null){
            return <div>no JSON loaded</div>
        }else{
            const commentHTML = json.commentsData.map((entry,index) => {
                
                return(
                    <div key={index}>
                        <a>{entry.isChecked}</a>
                        <input type="checkbox"  
                        //checked={entry.isChecked} 
                        // onChange={() => (console.log(index))}/>
                        onChange={() => (json.commentsData[index].isChecked = 1)}/>
                        <a style={comAuthorstyle}>{entry.author}</a>
                        <p style={paragraphstyle}> {entry.body} </p>
                    </div>
                    )
            })
            return(
                <div>
                    <a style={subAuthorstyle}>Posted by u/{json.submissionData.author}</a>
                    <div>
                        <p style={paragraphstyle}> {json.submissionData.selftext} </p>
                    </div>
                
                    <div>{commentHTML}</div>
                </div>
            )
        }
        
    }
}

export default RedditComment;