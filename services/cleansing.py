from libs.preprocessing import preprocess_text, preprocess_file
from services import AppServiceProject
from fastapi.responses import StreamingResponse
import io

from services.add_db import insert_text_to_db, insert_to_db_from_csv


class CleansingServices(AppServiceProject):
    async def cleansing(self, type, text):
        try:
            if type == "text":
                preprocess = preprocess_text(text)

                data = {
                    "data": preprocess
                }

                insert_text_to_db(preprocess)

                return self.success_response(data)
            else:
                preprocess = preprocess_file(text)
                stream = io.StringIO()
                preprocess.to_csv(stream, index=False)

                response = StreamingResponse(iter([stream.getvalue()]),
                                             media_type="text/csv"
                                             )
                response.headers["Content-Disposition"] = "attachment; filename=export.csv"

                insert_to_db_from_csv(preprocess)

                return response
        except Exception as e:
            return self.error_response(e)
