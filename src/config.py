from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Download Video Youtube"
    app_description: str = (
        "An open source API that adds a play button and a backdrop to a video"
        " thumbnail, provided the video"
        " ID.<br/>[Markdown-Videos](https://github.com/Snailedlt/Youtube-Thumbnail-Embedder)"
        " lets you embed videos into GitHub markdown with ease! <br/> <br/>"
        " Documentation alternatives: [Redoc](/redoc) | [Swagger](/docs) | [GitHub"
        " README](https://github.com/ikhramsyamsuri/video_convert/tree/main) "
    )
    contact: object = {
        "name": "Ikhram Syamsuri",
        "email": "Ikhramsyamsuri.main@gmail.com",
    }
    # The following get filled out by the .env file
    analytics_api_key: str = ""
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()