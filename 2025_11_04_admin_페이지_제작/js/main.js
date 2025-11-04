// ===== 데이터 =====
const product_data = [
  { category: "상의", brand: "Supreme",         product: "슈프림 박스로고 후드티",   price: "390,000" },
  { category: "하의", brand: "DIESEL",          product: "디젤 트랙 팬츠",         price: "188,000" },
  { category: "신발", brand: "Nike",            product: "에어포스 1",             price: "137,000" },
  { category: "패션잡화", brand: "Music&Goods", product: "빵빵이 키링",             price: "29,000" },

  { category: "상의", brand: "Stüssy",          product: "스투시 그래픽 반팔티",     price: "89,000" },
  { category: "상의", brand: "Ader Error",      product: "아더에러 오버핏 맨투맨",   price: "210,000" },
  { category: "하의", brand: "ADER",            product: "아더에러 와이드 조거팬츠", price: "195,000" },
  { category: "하의", brand: "Carhartt",        product: "칼하트 더블니 팬츠",       price: "165,000" },

  { category: "신발", brand: "New Balance",     product: "뉴발란스 530",            price: "129,000" },
  { category: "신발", brand: "Adidas",          product: "삼바 OG",                 price: "119,000" },
  { category: "패션잡화", brand: "Gentle Monster", product: "젠틀몬스터 선글라스",   price: "289,000" },
  { category: "패션잡화", brand: "Tiffany & Co.",  product: "티파니 팔찌",          price: "750,000" },

  { category: "아우터", brand: "North Face",    product: "노스페이스 눕시 패딩",     price: "399,000" },
  { category: "아우터", brand: "Moose Knuckles",product: "무스너클 파카",           price: "1,290,000" },
  { category: "상의",   brand: "Maison Kitsuné",product: "메종키츠네 폭스 티셔츠",   price: "128,000" },
  { category: "하의",   brand: "Nike",          product: "나이키 클럽 조거팬츠",     price: "79,000" }
];

// ===== 상태 =====
const PAGE_SIZE = 4;
let currentPage = 1;
let filtered = [...product_data];

// ===== 유틸 =====
function setTheme(root, themeSwitch, theme) {
  root.setAttribute('data-bs-theme', theme);
  localStorage.setItem('theme', theme);
  if (themeSwitch) themeSwitch.checked = theme === 'dark';
}

document.addEventListener('DOMContentLoaded', () => {
  // ===== DOM 캐시 (이제 DOM 준비 후에 가져오므로 null 안 뜸) =====
  const root = document.documentElement;
  const tbody = document.getElementById('product_data_Table');
  const paginationEl = document.getElementById('pagination');
  const categorySelect = document.getElementById('inlineFormSelectPref');
  const keywordInput = document.getElementById('keywordInput');
  const searchBtn = document.getElementById('searchBtn');
  const themeSwitch = document.getElementById('themeSwitch');

  // 안전 가드
  if (!tbody || !paginationEl) {
    console.error('필수 엘리먼트(tbody, pagination)가 없습니다. ID를 확인하세요.');
    return;
  }

  // ===== 렌더러 =====
  function renderTable(page = 1) {
    tbody.innerHTML = '';
    const start = (page - 1) * PAGE_SIZE;
    const end = start + PAGE_SIZE;
    const slice = filtered.slice(start, end);

    if (slice.length === 0) {
      const tr = document.createElement('tr');
      const td = document.createElement('td');
      td.colSpan = 4;
      td.className = 'text-center text-muted';
      td.textContent = '표시할 데이터가 없습니다.';
      tr.appendChild(td);
      tbody.appendChild(tr);
      return;
    }

    slice.forEach(item => {
      const row = tbody.insertRow();
      row.insertCell(0).textContent = item.category;
      row.insertCell(1).textContent = item.brand;
      row.insertCell(2).textContent = item.product;
      row.insertCell(3).textContent = item.price;
    });
  }

  function makePageItem(label, disabled, onClick, active = false) {
    const li = document.createElement('li');
    li.className = `page-item${disabled ? ' disabled' : ''}${active ? ' active' : ''}`;
    const a = document.createElement('a');
    a.className = 'page-link';
    a.href = '#';
    a.textContent = label;
    if (active) a.setAttribute('aria-current', 'page');
    a.addEventListener('click', (e) => {
      e.preventDefault();
      if (!disabled) onClick();
    });
    li.appendChild(a);
    return li;
  }

  function renderPagination() {
    const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    paginationEl.innerHTML = '';

    // Previous
    paginationEl.appendChild(
      makePageItem('Previous', currentPage === 1, () => goToPage(currentPage - 1))
    );

    // Numbers
    for (let i = 1; i <= totalPages; i++) {
      paginationEl.appendChild(
        makePageItem(String(i), false, () => goToPage(i), i === currentPage)
      );
    }

    // Next
    paginationEl.appendChild(
      makePageItem('Next', currentPage === totalPages, () => goToPage(currentPage + 1))
    );
  }

  function goToPage(page) {
    const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    currentPage = Math.min(Math.max(1, page), totalPages);
    renderTable(currentPage);
    renderPagination();
  }

  function applyFilter() {
    const cat = (categorySelect?.value || '').trim();
    const kw = (keywordInput?.value || '').trim().toLowerCase();

    filtered = product_data.filter(item => {
      const byCat = cat ? item.category === cat : true;
      const byKw = kw ? (item.product.toLowerCase().includes(kw) || item.brand.toLowerCase().includes(kw)) : true;
      return byCat && byKw;
    });

    currentPage = 1;
    renderTable(currentPage);
    renderPagination();
  }

  // ===== 초기화 =====
  // 카테고리 옵션
  if (categorySelect) {
    const categories = [...new Set(product_data.map(i => i.category))];
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = '카테고리';
    categorySelect.appendChild(defaultOption);
    categories.forEach(cat => {
      const opt = document.createElement('option');
      opt.value = cat;
      opt.textContent = cat;
      categorySelect.appendChild(opt);
    });
  }

  // 이벤트
  searchBtn?.addEventListener('click', applyFilter);
  categorySelect?.addEventListener('change', applyFilter);
  keywordInput?.addEventListener('keydown', (e) => { if (e.key === 'Enter') applyFilter(); });

  // 테마 스위치 & 초기 테마
  const savedTheme = localStorage.getItem('theme') || 'light';
  setTheme(root, themeSwitch, savedTheme);
  themeSwitch?.addEventListener('change', () => {
    setTheme(root, themeSwitch, themeSwitch.checked ? 'dark' : 'light');
  });

  // 최초 렌더
  renderTable(currentPage);
  renderPagination();
});