document.addEventListener('DOMContentLoaded', ()=>{
  const form = document.getElementById('todo-form');
  const input = document.getElementById('todo-input');
  const list = document.getElementById('todo-list');

  function renderItem(text, done=false){
    const li = document.createElement('li');
    const span = document.createElement('span');
    span.textContent = text;
    if(done) span.classList.add('done');

    const actions = document.createElement('div');
    actions.className = 'actions';

    const toggleBtn = document.createElement('button');
    toggleBtn.textContent = done ? '취소' : '완료';
    toggleBtn.addEventListener('click', ()=>{
      span.classList.toggle('done');
      toggleBtn.textContent = span.classList.contains('done') ? '취소' : '완료';
    });

    const delBtn = document.createElement('button');
    delBtn.textContent = '삭제';
    delBtn.addEventListener('click', ()=> li.remove());

    actions.appendChild(toggleBtn);
    actions.appendChild(delBtn);

    li.appendChild(span);
    li.appendChild(actions);
    list.appendChild(li);
  }

  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const v = input.value.trim();
    if(!v) return;
    renderItem(v);
    input.value = '';
    input.focus();
  });

  // demo starter items
  renderItem('리포지토리 정리하기');
  renderItem('코드 푸시하기');
});