import asyncio
from app.batch_calc import batch_average_threaded, batch_average_asyncio


def test_batch_threaded():
    ages = list(range(1, 21))  # 1..20
    results = batch_average_threaded(ages, batch_size=5, max_workers=2)
    assert len(results) == 4
    assert results[0] == sum(range(1, 6)) / 5


def test_batch_asyncio():
    ages = list(range(1, 11))
    res = asyncio.get_event_loop().run_until_complete(batch_average_asyncio(ages, batch_size=3))
    assert isinstance(res, list)
    assert len(res) == 4  # chunks: 3,3,3,1
