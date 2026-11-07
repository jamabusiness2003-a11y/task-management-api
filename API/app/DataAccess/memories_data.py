from datetime import datetime, timezone
from app.DataAccess.Models.User import User, Role

USERS: list[User] = [
    User(
        id=10,
        username="SuperJam",
        email="pizza_man@gmail.com",
        passwordHash="$2y$10$GFPTPBZmqVp0CFG9lt2wxuLLSxJFh9T8BfZ0atwXfw/ZVGqbgX6TC",
        firstName="Merzon",
        lastName="Jamario",
        role=Role.ADMINISTRATER,
        createdAt=datetime(2022, 9, 12, 19, 10, 10, tzinfo=timezone.utc)
    ),
    User(
        id=20,
        username="VelocityVibe",
        email="shadow.runner89@gmail.com",
        passwordHash="$2y$10$Bz0Bwf.Yhce37bnbIpwqhOF1kSvAU8dmB42a1d9lY0kv4sLjnvtT.",
        firstName="Vance",
        lastName="Ethan",
        role=Role.SUPPORT_STAFF,
        createdAt=datetime(2023, 10, 12, 19, 17, 30, tzinfo=timezone.utc)
    ),
    User(
        id=30,
        username="PixelPioneer",
        email="bright.meadows42@outlook.com",
        passwordHash="$2y$10$2SDw832OmCq2IPG39UPkU.MhjiVysNVBfU77rDec8TJs4dCq0apfm",
        firstName="Montgomery",
        lastName="Clara",
        role=Role.REGISTERED_USER,
        createdAt=datetime(2023, 9, 12, 20, 10, 10, tzinfo=timezone.utc)
    ),
    User(
        id=40,
        username="LunarEcho",
        email="quantum.drift@yahoo.com",
        passwordHash="$2y$10$W6Aqvs/p2C6tcBYob1Z6xO74Rm93p4NseJr9BYJPY7zdWRG.ff/AG",
        firstName="Mercer",
        lastName="Julian",
        role=Role.REGISTERED_USER,
        createdAt=datetime(2024, 4, 12, 9, 20, 10, tzinfo=timezone.utc)
    ),
    User(
        id=50,
        username="NeonNomad",
        email="cosmic.harbor17@proton.me",
        passwordHash="$2y$10$Mg5Xni9hvzEEG76RFGL1p.dggpTvNLfIUY2tANlBltGegyqdb7Nz.",
        firstName="Rostova",
        lastName="Elena",
        role=Role.REGISTERED_USER,
        createdAt=datetime(2025, 6, 12, 12, 10, 10, tzinfo=timezone.utc)
    ),
]