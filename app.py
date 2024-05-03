import streamlit as st
import pickle

def recommend_tv_serials(tv_serial_name, df, tf, cosine_sim):
    idx = df[df['Name'] == tv_serial_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar TV serials
    similar_tv_serials = [df.iloc[i[0]]['Name'] for i in sim_scores]
    return similar_tv_serials

def load_model():
    # Load the model from disk
    with open('cosine_similarity.pkl', 'rb') as f:
        df, tf, cosine_sim = pickle.load(f)
    return df, tf, cosine_sim

def main():
    st.title('TV Serial Recommender')

    # Load the model
    df, tf, cosine_sim = load_model()

    # Dropdown widget for selecting TV serial
    tv_serial_name = st.selectbox('Select TV Serial', df['Name'])

    if st.button('Recommend'):
        if tv_serial_name:
            similar_tv_serials = recommend_tv_serials(tv_serial_name, df, tf, cosine_sim)
            st.subheader(f'Recommended TV Serials for "{tv_serial_name}":')
            st.write(similar_tv_serials)
        else:
            st.warning('Please select a TV Serial')

if __name__ == '__main__':
    main()
