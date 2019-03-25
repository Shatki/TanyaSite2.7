////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// jQuery
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
let resizeId;

$(function() {
    "use strict";

    var $body = $("body");
    var $mainNavigation = $("#main-navigation");
    var $navigation = $mainNavigation.find(".navbar-nav");

    $navigation.find("> .nav-item > .nav-link").each(function (e) {
        var text = $(this).text();  //.replace(/\s/g, '');
        var firstLetter = text.substring(0,1);
        var hiddenLetters = text.substring(1);

        $(this).text("");
        $(this).append("<span>" + firstLetter + "</span>").append("<span class='ts-hidden'>" + hiddenLetters + "</span>");
        $(this).find(".ts-hidden").css("transition-delay", (e*50) + "ms");
    });

    $mainNavigation.on("mouseenter", function () {
        $body.addClass("nav-hovered");
    });

    $mainNavigation.on("mouseleave", function () {
        if( !$body.hasClass("toggled") ){
            $body.removeClass("nav-hovered");
        }
        $(this).find(".collapse").collapse("hide");
    });

    $(".navbar-toggler").on("click", function () {
        $("body").toggleClass("nav-hovered toggled");
    });

    $(".ts-promo-numbers").each(function () {
        $(this).isInViewport(function(status) {
            if (status === "entered") {
                for( var i=0; i < document.querySelectorAll(".odometer").length; i++ ){
                    var el = document.querySelectorAll('.odometer')[i];
                    el.innerHTML = el.getAttribute("data-odometer-final");
                }
            }
        });
    });

    $body.imagesLoaded( function() {
        $body.addClass("loading-done");
        $("[data-animate]").scrolla({
            mobile: true
        });
    });

    $(".ts-img-into-bg").each(function() {
        $(this).css("background-image", "url("+ $(this).find("img").attr("src") +")" );
    });

    $("[data-ts-delay]").each(function () {
        $(this).css("transition-delay", $(this).attr("data-ts-delay") ).css("animation-delay", $(this).attr("data-ts-delay") );
    });

//  Background

    $("[data-bg-color], [data-bg-image], [data-bg-particles]").each(function() {
        var $this = $(this);

        if( $this.hasClass("ts-separate-bg-element") ){
            $this.append('<div class="ts-background">');

            // Background Color

            if( $("[data-bg-color]") ){
                $this.find(".ts-background").css("background-color", $this.attr("data-bg-color") );
            }

            // Background Image

            if( $this.attr("data-bg-image") !== undefined ){
                $this.find(".ts-background").append('<div class="ts-background-image">');
                $this.find(".ts-background-image").css("background-image", "url("+ $this.attr("data-bg-image") +")" );
                $this.find(".ts-background-image").css("background-size", $this.attr("data-bg-size") );
                $this.find(".ts-background-image").css("background-position", $this.attr("data-bg-position") );
                $this.find(".ts-background-image").css("opacity", $this.attr("data-bg-image-opacity") );

                $this.find(".ts-background-image").css("background-size", $this.attr("data-bg-size") );
                $this.find(".ts-background-image").css("background-repeat", $this.attr("data-bg-repeat") );
                $this.find(".ts-background-image").css("background-position", $this.attr("data-bg-position") );
                $this.find(".ts-background-image").css("background-blend-mode", $this.attr("data-bg-blend-mode") );
            }

            // Parallax effect

            if( $this.attr("data-bg-parallax") !== undefined ){
                $this.find(".ts-background-image").addClass("ts-parallax-element");
            }
        }
        else {

            if(  $this.attr("data-bg-color") !== undefined ){
                $this.css("background-color", $this.attr("data-bg-color") );
                if( $this.hasClass("btn") ) {
                    $this.css("border-color", $this.attr("data-bg-color"));
                }
            }

            if( $this.attr("data-bg-image") !== undefined ){
                $this.css("background-image", "url("+ $this.attr("data-bg-image") +")" );

                $this.css("background-size", $this.attr("data-bg-size") );
                $this.css("background-repeat", $this.attr("data-bg-repeat") );
                $this.css("background-position", $this.attr("data-bg-position") );
                $this.css("background-blend-mode", $this.attr("data-bg-blend-mode") );
            }

        }
    });

//  Parallax Background Image

    $("[data-bg-parallax='scroll']").each(function() {
        var speed = $(this).attr("data-bg-parallax-speed");
        var $this = $(this);
        var isVisible;
        var backgroundPosition;

        $this.isInViewport(function(status) {
            if (status === "entered") {
                isVisible = 1;
                var position;

                $(window).on("scroll", function () {
                    if( isVisible === 1 ){
                        position = $(window).scrollTop() - $this.offset().top;
                        backgroundPosition = (100 - (Math.abs((-$(window).height()) - position) / ($(window).height()+$this.height()))*100);
                        if( $this.find(".ts-parallax-element").hasClass("ts-background-image") ){
                            $this.find(".ts-background-image.ts-parallax-element").css("background-position-y", (position/speed) + "px");
                        }
                        else {
                            $this.find(".ts-parallax-element").css("transform", "translateY(" +(position/speed)+ "px)");
                        }
                    }
                });
            }
            if (status === "leaved"){
                isVisible = 0;
            }
        });
    });

    // Owl Carousel

    initOwl();

    // Magnific Popup

    var $popupImage = $(".popup-image");

    if ( $popupImage.length > 0 ) {
        $popupImage.magnificPopup({
            type:'image',
            fixedContentPos: false,
            gallery: { enabled:true },
            removalDelay: 300,
            mainClass: 'mfp-fade',
            callbacks: {
                // This prevents pushing the entire page to the right after opening Magnific popup image
                open: function() {
                    $(".page-wrapper, .navbar-nav").css("margin-right", getScrollBarWidth());
                },
                close: function() {
                    $(".page-wrapper, .navbar-nav").css("margin-right", 0);
                }
            }
        });
    }

    var $videoPopup = $(".video-popup");

    if ( $videoPopup.length > 0 ) {
        $videoPopup.magnificPopup({
            type: "iframe",
            removalDelay: 300,
            mainClass: "mfp-fade",
            overflowY: "hidden",
            iframe: {
                markup: '<div class="mfp-iframe-scaler">'+
                '<div class="mfp-close"></div>'+
                '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
                '</div>',
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: 'v=',
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: '/',
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    },
                    gmaps: {
                        index: '//maps.google.',
                        src: '%id%&output=embed'
                    }
                },
                srcAction: 'iframe_src'
            }
        });
    }

    // animation of sending
    $(".ts-form [type='submit']").each(function(){
        var text = $(this).text();
        $(this).html("").append("<span>"+ text +"</span>").prepend("<div class='status'><i class='fas fa-circle-notch fa-spin spinner'></i></div>");
    });

    $(".ts-form-email .btn[type='submit']").on("click", function(e){
        var $button = $(this);
        var $form = $(this).closest("form");
        var path = $(this).closest("form").attr("data-path");
        $form.validate({
            submitHandler: function() {
                $button.addClass("processing");
                $.post(path, $form.serialize(),  function(response) {
                    let $form = $button.closest("form");
                    if(response === true){
                        $form.trigger("reset");
                        let div = '<div class="container">Ваше сообщение успешно отправлено</div>';
                        $.createModal({
                            title:'Обратная связь',
                            message: div,
                            closeButton:true,
                            scrollable:false
                        });
                        $button.addClass("done").removeClass('processing').
                        prop("disabled", true);
                        return false;
                    }else{
                        // Не отправляется
                        $button.addClass("done").
                        prop("disabled", true);
                    }
                });
                return false;
            }
        });
    });

    //$("form:not(.ts-form-email)").each(function(){
    //    $(this).validate();
    //});
    
    // News
    // Отправка комментариев
    $(".ts-form-comment").validate({
            submitHandler: function(form) {
                let $form = $(form);
                let $button = $(form).find('.btn');
                var path = $form.attr("data-path");
                $button.addClass("processing");
                $.post(path, $form.serialize(),  function(response) {
                    //let $form = $button.closest("form");
                    if(response === true){
                        $form.trigger("reset");
                        let div = '<div class="container">Ваш комментарий отправлен. Он будет виден после модерации.</div>';
                        $.createModal({
                            title:'Обсуждение новостей',
                            message: div,
                            closeButton:true,
                            scrollable:false
                        });
                        $button.addClass("done").removeClass('processing').
                        prop("disabled", true);
                        return false;
                    }else{
                        let div = '<div class="container">При отправке возникла ошибка.</div>';
                        $.createModal({
                            title:'Обсуждение новостей',
                            message: div,
                            closeButton:true,
                            scrollable:false
                        });
                    }
                });
                // Стандартно завершаем после удачной отправки
                return false;
            }
    });

    $(".link-reply").on("click", function(e){
        let $button = $(this);
        let $div = $button.closest("div");
        let comment_id = $div.attr('id');
        let target_id = '#form-reply-' + comment_id;
        let $target = $(target_id);
        //$target.show();
        $("#leave-reply").appendTo($target);
        // answer on comment #
        $('#form-news-reply-comment').attr("value", comment_id);
        $('#leave-reply-header-text').hide();
        $('#form-news-cancel-reply-to').show();
        return false;
    });

    $("#form-news-cancel-reply-to").on("click", function(e){
        let $button = $(this);
        let $section = $button.closest("section");
        let $target = $('#reply-form-common');
        $section.appendTo($target);
        $('#form-news-reply-comment').attr("value", "");
        $('#leave-reply-header-text').show();
        $('#form-news-cancel-reply-to').hide();
        return false;
    });

    $('.btn-outline-primary').hide(); // Отключение видимости дополнительных кнопок

    // Other

    $(".progress").each(function(){
        var $this = $(this);
        $this.find(".ts-progress-value").text( $this.attr("data-progress-width") );
        $this.isInViewport(function(status) {
            if (status === "entered") {
                $this.find(".progress-bar").width( $this.attr("data-progress-width") );
                $this.find(".ts-progress-value").css("left", $this.attr("data-progress-width"));
            }
        });
    });

    if( $(".ts-gallery__masonry").length ){
        let container = $(".ts-masonry");
        container.imagesLoaded( function() {
            container.masonry({
                gutter: 15,
                itemSelector: '.ts-gallery__masonry'
            });
        });
    }
    // On RESIZE actions

    $(window).on("resize", function(){
        clearTimeout(resizeId);
        resizeId = setTimeout(doneResizing, 250);
    });


    /*
* Here is how you use it
*/

    $('.doc-view').on('click',function(){
        var pdf_link = $(this).attr('href');
        var iframe = '<div class="iframe-container"><iframe src="'+pdf_link+'"></iframe></div>';
        $.createModal({
            title:'Предпросмотр документа',
            message: iframe,
            closeButton:true,
            scrollable:false
        });
        return false;
    });

});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Functions
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Do after resize

function doneResizing(){
    $(".owl-carousel").trigger('next.owl.carousel');
}

// Smooth Scroll
$(".ts-scroll").on("click", function(event) {
    if (
        location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '')
        &&
        location.hostname === this.hostname
    ) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            event.preventDefault();
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 1000, function() {
                var $target = $(target);
                $target.focus();
                if ($target.is(":focus")) {
                    return false;
                } else {
                    $target.attr('tabindex','-1');
                    $target.focus();
                }
            });
        }
    }
});

// Return scrollbar width

function getScrollBarWidth () {
    var $outer = $('<div>').css({visibility: 'hidden', width: 100, overflow: 'scroll'}).appendTo('body'),
        widthWithScroll = $('<div>').css({width: '100%'}).appendTo($outer).outerWidth();
    $outer.remove();
    return 100 - widthWithScroll;
}

function initOwl(){
    var $owlCarousel = $(".owl-carousel");

    if( $owlCarousel.length ){
        $owlCarousel.each(function() {

            var items = parseInt( $(this).attr("data-owl-items"), 10);
            if( !items ) items = 1;

            var nav = parseInt( $(this).attr("data-owl-nav"), 2);
            if( !nav ) nav = 0;

            var dots = parseInt( $(this).attr("data-owl-dots"), 2);
            if( !dots ) dots = 0;

            var center = parseInt( $(this).attr("data-owl-center"), 2);
            if( !center ) center = 0;

            var loop = parseInt( $(this).attr("data-owl-loop"), 2);
            if( !loop ) loop = 0;

            var margin = parseInt( $(this).attr("data-owl-margin"), 2);
            if( !margin ) margin = 0;

            var autoWidth = parseInt( $(this).attr("data-owl-auto-width"), 2);
            if( !autoWidth ) autoWidth = 0;

            var navContainer = $(this).attr("data-owl-nav-container");
            if( !navContainer ) navContainer = 0;

            var autoplay = parseInt( $(this).attr("data-owl-autoplay"), 2);
            if( !autoplay ) autoplay = 0;

            var autoplayTimeOut = parseInt( $(this).attr("data-owl-autoplay-timeout"), 10);
            if( !autoplayTimeOut ) autoplayTimeOut = 5000;

            var autoHeight = parseInt( $(this).attr("data-owl-auto-height"), 2);
            if( !autoHeight ) autoHeight = 0;

            var fadeOut = $(this).attr("data-owl-fadeout");
            if( !fadeOut ) fadeOut = 0;
            else fadeOut = "fadeOut";

            if( $("body").hasClass("rtl") ) var rtl = true;
            else rtl = false;

            if( items === 1 ){
                $(this).owlCarousel({
                    navContainer: navContainer,
                    animateOut: fadeOut,
                    autoplayTimeout: autoplayTimeOut,
                    autoplay: 1,
                    autoHeight: autoHeight,
                    center: center,
                    loop: loop,
                    margin: margin,
                    autoWidth: autoWidth,
                    items: 1,
                    nav: nav,
                    dots: dots,
                    rtl: rtl,
                    navText: []
                });
            }
            else {
                $(this).owlCarousel({
                    navContainer: navContainer,
                    animateOut: fadeOut,
                    autoplayTimeout: autoplayTimeOut,
                    autoplay: autoplay,
                    autoHeight: autoHeight,
                    center: center,
                    loop: loop,
                    margin: margin,
                    autoWidth: autoWidth,
                    items: 1,
                    nav: nav,
                    dots: dots,
                    rtl: rtl,
                    navText: [],
                    responsive: {
                        1199: {
                            items: items
                        },
                        992: {
                            items: 3
                        },
                        768: {
                            items: 2
                        },
                        0: {
                            items: 1
                        }
                    }
                });
            }

            if( $(this).find(".owl-item").length === 1 ){
                $(this).find(".owl-nav").css( { "opacity": 0,"pointer-events": "none"} );
            }

        });
    }
}