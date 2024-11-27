from models.process_model import ProcessPolling



def main():

    process = ProcessPolling()
    process.start_polling()
    

if __name__ == '__main__':
    main()
