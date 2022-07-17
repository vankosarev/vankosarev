import vk_api

session = vk_api.VkApi(token="5b0baf53e824947ab451a7866981672089527c8412a61ccdd4da5f448528fd771749aa02ef22f01f7204d")
vk = session.get_api()


def set_status(user_id):
    status = session.method("status.get",{"user_id":user_id})
    print(status)

set_status(171795624)
