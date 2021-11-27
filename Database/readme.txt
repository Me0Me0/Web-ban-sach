Mô tả các bảng trong database

user(id, username, password, name, dob, address, phone, email, avt_link): bảng này lưu thông tin của người dùng
id: id của mỗi người dùng, là duy nhất
username: tên đăng nhập của người dùng, là duy nhất
password: mật khẩu của người dùng
name: họ tên người dùng
dob: ngày tháng năm sinh của người dùng
address: địa chỉ của người dùng
phone: số điện thoại của người dùng
email: email của người dùng

	contact(id, user_id, create, title, content, status): bảng này lưu thông tin của liên hệ từ người dùng tới admin
id: id của mỗi liên hệ, là duy nhất
user_id: id của người dùng liên hệ với admin
create: ngày tạo liên hệ
title: tiêu đề của liên hệ
content: nội dung của liên hệ
status: trạng thái của liên hệ, quy định các trạng thái chưa xử lý/đang xử lý/đã xử lý bằng các số nguyên chẳng hạn

product(id, name, cate_id, rating, description, detail, author, number_of_pages, publishing_year, publishing_company, cover_image, store_id, quantity, price): bảng này lưu thông tin của sản phẩm (là cuốn sách)
id: id của mỗi sản phẩm, là duy nhất
name: tên của mỗi sản phẩm
cate_id: id của thể loại sản phẩm
rating: mức độ đánh giá sản phẩm
description: mô tả về ngắn về sản phẩm
detail: thông tin, mô tả chi tiết về sản phẩm
author: tên tác giả
number_of_pages: số trang
publishing_year: năm xuất bản
publishing_company: nhà xuất bản
cover_image: liên kết dẫn đến ảnh bìa của sản phẩm
store_id: id của cửa hàng sở hữu sản phẩm
quantity: số lượng sản phẩm
price: đơn giá của sản phẩm

store(id, name, owner, phone, email, rating, description): bảng này lưu thông tin của cửa hàng
id: id của mỗi cửa hàng, là duy nhất
name: tên của mỗi cửa hàng
owner: id của chủ sở hữu cửa hàng
phone: số điện thoại của cửa hàng
email: email của cửa hàng
rating: mức độ đánh giá cửa hàng
description: mô tả, giới thiệu về cửa hàng

cart(id, owner): bảng này lưu thông tin của giỏ hàng
id: id của mỗi giỏ hàng, là duy nhất
owner: id của chủ sở hữu giỏ hàng

	admin(id, username, pass, name): bảng này lưu thông tin của quản trị viên
id: id của quản trị viên, là duy nhất
username: tên đăng nhập của quản trị viên, là duy nhất
pass: mật khẩu của quản trị viên
name: họ và tên của quản trị viên

order_detail(id, owner, status, toast_cost, recipient_name, recipient_phone, recipient_address, province_id, district_id, ward_id): bảng này lưu thông tin của đơn hàng
id: id của mỗi đơn hàng, là duy nhất
owner: chủ sở hữu của đơn hàng
status: trạng thái đơn hàng (đang chờ cửa hàng xác nhận/đang giao hàng/đã giao thành công/đã hủy… được quy định bằng các số nguyên)
toast_cost: tổng tiền của đơn hàng
recipient_name, recipient_phone, recipient_address lần lượt là họ tên, số điện thoại, địa chỉ của người nhận hàng
province_id, district_id, ward_id lần lượt là mã tỉnh/thành phố, mã thành phố/quận/huyện, mã xã/phường của người nhận hàng

product_image(id, image_link): bảng này lưu các hình ảnh của sản phẩm
id: id của sản phẩm
image_link: liên kết dẫn đến hình ảnh của sản phẩm

	category(id, name): bảng này lưu thông tin về thể loại sản phẩm
id: id của mỗi thể loại, là duy nhất
name: tên thể loại

	cart_product(cart_id, product_id, quantity): bảng này lưu những sản phẩm có trong giỏ hàng
cart_id: id của giỏ hàng
product_id: id của sản phẩm
quantity: số lượng sản phẩm

	order_product(order_id, product_id, quantity): bảng này lưu những sản phẩm có trong hóa đơn
order_id: id của hóa đơn (đơn hàng)
product_id: id của sản phẩm
quantity: số lượng sản phẩm
	province(id, _name, _code): bảng này lưu thông tin các tỉnh/thành phố trực thuộc trung ương trong nước
id: id của mỗi tỉnh/thành phố, là duy nhất
_name: tên tỉnhthành phố, là duy nhất
_code: mã tỉnh/thành phố, là duy nhất

	district(id, _name, _prefix, _province_id): bảng này lưu thông tin các thành phố/huyện/quận trực thuộc tỉnh/thành phố trực thuộc trung ương
id: id của mỗi thành phố/huyện/quận, là duy nhất
_name: tên thành phố/huyện/quận
_prefix: tiền tố tên thành phố/huyện/quận
_province_id: id của tỉnh/thành phố trực thuộc trung ương mà thành phố/huyện/quận này thuộc về

	ward(id, _name, _prefix, _province_id, _district_id): bảng này lưu thông tin phường/xã thuộc thành phố/huyện/quận
id: id của mỗi phường/xã, là duy nhất
_name: tên phường/xã
_prefix: tiền tố tên phường/xã
_province_id: id của tỉnh/thành phố trực thuộc trung ương mà phường/xã này thuộc về
_district_id: id của thành phố/huyện/quận trực thuộc tỉnh/thành phố trực thuộc trung ương mà phường/xã này thuộc về

Mô tả về kiểu dữ liệu của các thuộc tính xem trong database diagram
