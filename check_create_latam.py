import pandas as pd
import os

paises_latam = ['Argentina','Bolivia','Brazil','Brasil','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','República Dominicana','Ecuador','El Salvador','Guatemala','Honduras','Mexico','México','Nicaragua','Panama','Panamá','Paraguay','Peru','Perú','Puerto Rico','Uruguay','Venezuela']

infile = 'global_electricity_production_data.csv'
outfile = 'latam_electricity_production_data.csv'

if not os.path.exists(infile):
    print(f'Missing input: {infile}')
    raise SystemExit(1)

try:
    df = pd.read_csv(infile)
except Exception as e:
    print('READ ERROR:', e)
    raise

col = next((c for c in df.columns if 'country' in c.lower() or 'pais' in c.lower()), None)
if col is None:
    print('No se encontró columna de país. Columnas disponibles:', list(df.columns))
    df_latam = df.iloc[0:0]
else:
    df_latam = df[df[col].isin(paises_latam)]

print('Registros LATAM:', len(df_latam))

df_latam.to_csv(outfile, index=False)
print('Wrote', outfile)
