const deleteForm = document.querySelector('.form-delete');

if(deleteForm) {
    deleteForm.addEventListener('submit', function(event) {
        event.preventDefault();
    
        iziToast.question({
            timeout: 20000,
            close: true,
            overlay: true,
            displayMode: 'once',
            id: 'question',
            zindex: 999,
            title: 'Delete your question',
            message: 'Are you sure?',
            position: 'center',
            buttons: [
                ['<button><b>YES</b></button>', function (instance, toast) {

                    deleteForm.submit();
         
                    instance.hide({ transitionOut: 'fadeOut' }, toast, 'submit');
         
                }, true],
                ['<button >NO</button>', function (instance, toast) {
         
                    instance.hide({ transitionOut: 'fadeOut' }, toast, 'cancel');
         
                }],
            ],
            onClosing: function(instance, toast, closedBy){
            
            },
            onClosed: function(instance, toast, closedBy){
               
            }
        });
    });
}

