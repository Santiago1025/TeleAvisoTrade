from metaapi_cloud_sdk import MetaApi
import asyncio
import logging

API_KEY = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJlMTAwYTQyNjdjNzM4NjRlMWE3OWMxNDNiZTVmMjdkMyIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiZTEwMGE0MjY3YzczODY0ZTFhNzljMTQzYmU1ZjI3ZDMiLCJpYXQiOjE3MDEzMjY0MjR9.GrNjT3nuTnS33nx4X8jwQ72Lt5k502fKxXNlXraOcQLcfrFrPCMlOc6BhjBvMhPVGvD7NVpDI2yUMOw8VtGCeUMmUaVHPmWmxX5-E4aBKFiPsRHPqD5ngCsFgYULEzucZmHIEik6FaQDmZ1odEIuQyBnmFWAmFYs4d05IhXLz-Lj1awnIsoTcVHxLVm_41q_b-P5ikT08COjbczwl9_3TN2HC09c8_lcY1iaZQbQ15GoO_SCm1xUDdq_E8mnHOuLBYoWO_cZid3JQCB6eKNKjXDNdGm9lvr7k13m4GkN-r8qQn0ER8LFipMRyRYxobl_atc5DP0jyJWHfVJST1Y2xd_bpc1jIGAhc7s6mUIMtgzUVyoru9BEo0FFVfiCo6di3vQQnfKGhOd3IDAnOxYMICOvdFj8zXI6ZcUq0etEBOPp7zAxRGS1nulYjt96TyXnYZ_w_QyAF7MYpOYngxzYgAV7-VZHEdvcC9JU6oElwCVPLb-sFKmGsdsZieIsuToTS0eNlwzqagVJNZ6ytZQaN9bzGVk7W4tQjHfExc83XB4Aqkw3D69-jrCcyw5upQwOzbUI26OxIjGe6uo_mHmmC84KK0e4YpXcxeeWsCrR8RTx0kIudp9M8LmtHJZS_Zkg-eOn0nXNdHRKRICjO1a4PFtyDQfMggvVBgGWuW6u7rw'

ACCOUNT_ID = '5dc8e4fd-b397-48c2-9250-9b8cba28d193'


#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    api = MetaApi(API_KEY)
    try:
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            # Desplegar la cuenta si aún no está desplegada
            logger.info('Deploying account')
            await account.deploy()

            # Esperar hasta que la cuenta se haya desplegado y conectado al broker
            logger.info('Waiting for the account to be deployed and connected to broker...')
            await account.wait_connected()

        # Conectar a la API de MetaApi
        connection = account.get_rpc_connection()
        await connection.connect()

        while True:
            # Esperar hasta que el estado del terminal se haya sincronizado con el estado local
            logger.info('Esperando que SDK se sincronice con el estado del terminal ...')
            await connection.wait_synchronized()

            # Obtener información de la cuenta desde el servidor de MetaTrader
            account_information = await connection.get_account_information()
            balance = account_information['equity']

            print(f'El balance es: {balance}')
            
            # Esperar un minuto antes de realizar la próxima actualización
            await asyncio.sleep(60)
    
    except Exception as error:
        logger.error(f'Error: {error}')
        print(f"There was an issue with the connection 😕\n\nError Message:\n{error}")

if __name__ == '__main__':
    asyncio.run(main())
