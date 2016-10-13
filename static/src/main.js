var Item = React.createClass({
  render: function () {
    return (
      <a href="#" className="list-group-item">
        <p className="list-group-item-text">{this.props.name}</p>
      </a>
    )
  }
});

var List = React.createClass({
  render: function () {
    var items = this.props.items.map(function (item) {
      return (
        <Item key={item.id} name={item.name}/>
      );
    });

    return (
      <div className="col-md-3">
        <div className="list-group">
          <h4>{this.props.name || 'Untitled List'}</h4>
          {items}
        </div>
      </div>
    )
  }
});

var ToDoComponent = React.createClass({
  getInitialState: function () {
    return {data: []};
  },

  componentDidMount: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function (data) {
        this.setState({data: data});
      }.bind(this)
    });
  },

  render: function () {
    var lists = this.state.data.map(function (list) {
      return (
        <List key={list.id} name={list.name} items={list.items} />
      );
    });

    return (
      <div className="row">
        <h3>All your lists</h3>
        {lists}
      </div>
    )
  }
});

ReactDOM.render(
  <ToDoComponent url='/api/list/' />,
  document.getElementById('react-app')
);
