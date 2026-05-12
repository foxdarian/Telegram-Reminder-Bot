import aiosqlite


DB_NAME = "reminders.db"

async def init_db() -> None:
    """Initialize the database and create the reminders table if it doesn't exist."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                delay INTEGER NOT NULL
            )
        """)
        await db.commit()

async def save_reminder(user_id: int, text: str, delay: int) -> None:
    """Save a reminder to the database."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO reminders (user_id, text, delay) VALUES (?, ?, ?)", (user_id, text, delay))
        await db.commit()