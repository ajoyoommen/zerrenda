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
  render: function () {
    var list_a = [
      {id: 1, name: 'learn to code', items: [
        {id: 2, name: 'learn syntax'},
        {id: 3, name: 'learn why it works'}
      ]},
      {id: 4, name: 'learn to debug', items:[
        {id:5, name: 'find the approximate location'},
        {id:6, name: 'follow the error trail'}
      ]}
    ];

    var lists = list_a.map(function (list) {
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
  <ToDoComponent />,
  document.getElementById('react-app')
);
