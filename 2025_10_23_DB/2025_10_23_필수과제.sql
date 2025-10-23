-- 1.employees 테이블을 생성해주세요
CREATE TABLE employees (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  position VARCHAR(100) NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 직원 데이터를 employees에 추가해주세요
INSERT INTO employees (name, position, salary) VALUES
('혜린', 'PM',        90000.00),
('은우', 'Frontend',  80000.00),
('가을', 'Backend',   92000.00),
('지수', 'Frontend',   7800.00),   -- 사용자가 준 값 그대로 반영 (7,800)
('민혁', 'Frontend',  96000.00),
('하온', 'Backend',  130000.00);

-- 모든 직원의 이름과 연봉 정봔을 조회하는 쿼리를 작성해주세요
SELECT name, salary
FROM employees;

-- Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
SELECT name, salary
FROM employees
WHERE position = 'Frontend'
  AND salary <= 90000;
  
-- PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
  UPDATE employees
SET salary = ROUND(salary * 1.10, 2)
WHERE position = 'PM';

-- 모든 Backend' 직책을 가진 직원의 연봉을 5% 인상하세요.
UPDATE employees
SET salary = ROUND(salary * 1.05, 2)
WHERE position = 'Backend';

select * from employees;

-- 민혁 사원의 데이터를 삭제하세요
DELETE FROM employees
WHERE name = '민혁';

-- 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
SELECT
  position,
  ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY position
ORDER BY position;

-- employees 테이블 삭제하세요.
drop table employees;