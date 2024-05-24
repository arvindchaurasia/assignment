## Assignment

### git clone run below command

--  git clone https://github.com/arvindchaurasia/assignment testassignment

### setup local environment
--  python3 -m venv env

--  source env/bin/activate
    
### For install all dependencies run below command 

--  pip3 install -r requirement.txt

### For run uvicorn server run below command

--  uvicorn main:app --reload


-- request 
	   {
		"batchid": "id0101",
		"payload": [[1, 2], [3, 4]]
		}


--  or we can run below curl command

    curl -X 'POST' \
	  'http://127.0.0.1:8000/addlist' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	"batchid": "id0101",
	"payload": [[1, 2], [3, 4]]
	}'
### for run unittest run below command
    cd unittest
--  pytest
   
