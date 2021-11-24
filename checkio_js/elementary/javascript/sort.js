let array13 = [
    {first: 'Joe',
     last: 'Smith'},
    {first: 'Anne',
     last: 'Smith'},
    {first: 'Tom',
     last: 'Doe'},
    {first: 'Anne',
     last: 'Doe'},]

console.log(array13)

 array13.sort((a,b) => {
     let nameA = a.first.toLowerCase()
     let nameB = b.first.toLowerCase()

     return (
     nameA < nameB ? -1 :
     nameA > nameB ? 1 :
     0)
})

console.log(array13)
