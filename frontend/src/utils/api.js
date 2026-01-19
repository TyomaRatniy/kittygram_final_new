const BASE_URL = "/api";

function request(url, options) {
  return fetch(url, options).then(checkResponse);
}

function checkResponse(res) {
  if (res.ok) {
    return res.json();
  }
  return Promise.reject(res.status);
}

export const register = (email, password) => {
  return request(`${BASE_URL}/users/`, {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });
};

export const authorize = (email, password) => {
  return request(`${BASE_URL}/jwt/create/`, {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });
};

export const getUser = () => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/users/me/`, {
    method: "GET",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    }
  });
};

export const sendCard = (card) => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/cards/`, {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(card)
  });
};

export const getCards = () => {
  return request(`${BASE_URL}/cards/`, {
    method: "GET",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
  });
};

export const getCardById = (id) => {
  return request(`${BASE_URL}/cards/${id}/`, {
    method: "GET",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
  });
};

export const updateCard = (id, card) => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/cards/${id}/`, {
    method: "PATCH",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(card)
  });
};

export const deleteCard = (id) => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/cards/${id}/`, {
    method: "DELETE",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    }
  });
};

export const likeCard = (id) => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/cards/${id}/likes/`, {
    method: "PUT",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    }
  });
};

export const unlikeCard = (id) => {
  const token = localStorage.getItem("token");
  return request(`${BASE_URL}/cards/${id}/likes/`, {
    method: "DELETE",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    }
  });
};
