import os
from dotenv import dotenv_values

values = {
    **dotenv_values(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.env")
    )
}
