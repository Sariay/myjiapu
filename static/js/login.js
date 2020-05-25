jQuery(document).ready(function ($) {

    var focusProcessor = function () {

        $('.login-page .img__btn').on('click', function () {
            $('.login-page .content').toggleClass('s--signup');
        });

        if (PAGE_TYPE == "SIGNUP"){
            $('.login-page .img__btn').trigger("click");
        }

        $('.login-page input').focus(function () {

            $(this).removeClass('input-error').addClass('input-active')
            $('.errorlist, .error-message').text('')
        });

        $('.login-page input').blur(function () {
                $(this).removeClass('input-active');
        });
    };

    var refreshVerifyCode = function () {
        if($('#verify #id_captcha_1').length){
            $('#verify #id_captcha_1').attr("placeholder","验证码");
        }

        if($('#verify').hasClass("verity-error")){
            $('#verify #id_captcha_1').addClass('input-error');
            console.info("添加类成功！")
        }

        $('#verify img.captcha').on('click', function(){
             $.ajax({
                url: "/captcha/refresh/?"+Math.random(),
                type: "GET",
                async: true,
                timeout: 10000,
                success: function (result) {
                    $('#verify img.captcha').attr("src",result.image_url);
                    $('#verify #id_captcha_0').attr("value",result.key);
                },
                error: function () {
                    alert("验证码获取失败，请再次点击或检查网络！")
                }
            })
        });
    };

    (function (Init) {
        focusProcessor();
        refreshVerifyCode();
    })();
});