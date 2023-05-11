from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psycopg2


app = FastAPI()
count = 5

conn = psycopg2.connect(database="testdb",
                        host="localhost",
                        user="postgres",
                        password="mysecretpassword",
                        port="5432")


@app.get("/")
def read_root(salary:int = 0):
    global count
    count -= 1
    # return {"Hello": "Priyanka", "Count": count}
    cursor = conn.cursor()
    cursor.execute(f"select * from company where salary > {salary};")
    names = []
    for row in cursor:
        name = row[1]
        names.append(name)
    # name_list = ",".join(names)
    # return "<h1> My name is Priyanka and I am not a terrorist. But " + (str(count) if count > 0 else "Boom") + "</h1>"
    return {"names": names}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        reload=True,
        # factory=True,
        host="0.0.0.0",
        port=8003,
        forwarded_allow_ips="*",
    )