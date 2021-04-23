import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://kpj_mongo_admin:<password>@api-serving.knab2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students_collection")