$('#submit').click(addCupcake)

async function addCupcake() {
    await axios.post('/api/cupcakes')
}


$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).data('id');
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}