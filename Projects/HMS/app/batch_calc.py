from concurrent.futures import ThreadPoolExecutor
import asyncio
from app.crud import get_all_patients

def average_age_batch(patients):
    if not patients:
        return 0
    return sum(p.age for p in patients) / len(patients)

def batch_average_age_threadpool(batch_size=10):
    patients = get_all_patients()
    results = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(0, len(patients), batch_size):
            batch = patients[i:i + batch_size]
            futures.append(executor.submit(average_age_batch, batch))
        for future in futures:
            results.append(future.result())
    return results

async def average_age_async(patients):
    await asyncio.sleep(0)  # simulate async op
    return average_age_batch(patients)

async def batch_average_age_asyncio(batch_size=10):
    patients = get_all_patients()
    tasks = []
    for i in range(0, len(patients), batch_size):
        batch = patients[i:i + batch_size]
        tasks.append(average_age_async(batch))
    results = await asyncio.gather(*tasks)
    return results