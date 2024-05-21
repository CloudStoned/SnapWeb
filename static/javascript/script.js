document.addEventListener("DOMContentLoaded", function() {
    const popupOverlay = document.querySelector('.popup-overlay');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const closeBtn = document.querySelector('.close-btn');
    const guideBtn = document.getElementById('guide-btn');
    const uploadInput = document.getElementById('upload');
    const uploadImagePreview = document.getElementById('upload-image-preview');

    const slidesContent = [
        {
            title: 'Welcome to Snapfolia',
            content: 'Here are some reminders to utilize the full potential of the app.',
            subtitle: 'Please upload a closeup picture of the leaf.',
            images: [
                '/static/assets/guide/slide1_yes.jpg',
                '/static/assets/guide/slide1_no.jpg'
            ]
        },
        {
            title: 'Welcome to Snapfolia',
            content: 'Here are some reminders to utilize the full potential of the app.',
            subtitle: 'Please upload an image that is centered on the leaf.',
            image: '/static/assets/guide/slide2_yes.jpg',
            alt: 'Second slide image',
            secondImage: '/static/assets/guide/slide2_no.jpg'
        },
        {
            title: 'Welcome to Snapfolia',
            content: 'Here are some reminders to utilize the full potential of the app.',
            subtitle: 'Please avoid uploading blurry photos.',
            image: '/static/assets/guide/slide3_yes.jpg',
            alt: 'Third slide image',
            secondImage: '/static/assets/guide/slide3_no.jpg'
        }
    ];

    let slideIndex = 0;

    function closePopup() {
        popupOverlay.style.display = 'none';
    }

    function showPrevSlide() {
        slideIndex--;
        if (slideIndex < 0) {
            slideIndex = slidesContent.length - 1;
        }
        updatePopup();
    }

    function showNextSlide() {
        slideIndex++;
        if (slideIndex >= slidesContent.length) {
            slideIndex = 0;
        }
        updatePopup();
    }

    function updatePopup() {
        const currentSlide = slidesContent[slideIndex];
        document.getElementById('popup-title').textContent = currentSlide.title;
        document.getElementById('popup-content').textContent = currentSlide.content;
        document.getElementById('popup-subtitle').textContent = currentSlide.subtitle;

        if (currentSlide.images) {
            document.getElementById('popup-image').src = currentSlide.images[0];
            document.getElementById('popup-image2').src = currentSlide.images[1];
        } else {
            document.getElementById('popup-image').src = currentSlide.image;
            document.getElementById('popup-image2').src = currentSlide.secondImage;
        }
    }

    prevBtn.addEventListener('click', showPrevSlide);
    nextBtn.addEventListener('click', showNextSlide);
    closeBtn.addEventListener('click', closePopup);

    // Show the popup when the page loads
    popupOverlay.style.display = 'flex';
    updatePopup();

    guideBtn.addEventListener('click', function() {
        popupOverlay.style.display = 'flex';
        updatePopup();
    });

    uploadInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                uploadImagePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    const leafPopups = document.getElementById('leaf-popups');

    const leafData = {
        dau: {
            additionalImage1: '/static/assets/leaves/Dau_1.png',
            additionalImage2: '/static/assets/leaves/Dau_2.png',
            title: 'Dau Leaf',
            content: 'Dao is a large tree, growing 30 meters or taller, with the trunk 1 meter or more in diameter. Leaves are alternate and pinnately compound. Leaflets are smooth, oblong, 5 to 7 pairs, up to 15 centimeters long and 4 centimeters wide, pointed at the apex, and abruptly tapered at the base. Flowers are small, white, and fragrant, hanging in lax panicles. Fruit is globose, green turning yellow when ripe with oval markings on the upper side of the fruit, about 2 to 3 centimeters in diameter.  In the Philippines, the municipality of Dao, Capiz and barangay of Dau in Mabalacat, Pampanga are named after the dao tree. The genus name derives from Greek words for drago (dragon) and melon, referring to the fruit. The species epithet dao derives from the Philippine vernacular name for the tree.',
            mainImage: '/static/assets/leaves/dau.png',
            alt: 'Dau Leaf'
        },
        kaliyos: {
            title: 'Kaliyos Leaf',
            content: 'Kalios is a rigid and densely branched tree, 4 to 15 meters high. Leaves are oblong-ovate to subrhomboid, 4 to 12 centimeters long, very rough on both sides, with finely toothed margins, the tip blunt or tapering to a point, the base narrowed. Male flowers are in roundish heads, 4 to 7 millimeters in diameter, short-peduncled, greenish-yellow or nearly white. Female flowers are peduncled, usually in pairs, green, the sepals accrescent and nearly enclosing the fruit. Fruit is ovoid, 8 to 10 millimeters long, pale yellow, the pericarp soft and fleshy. Seed is ovoid, 5 to 6 millimeters long.  In thickets at low and medium altitudes, especially in regions with long dry seasons, from northern Luzon to Palawan and Mindanao.  ',
            mainImage: '/static/assets/leaves/kaliyos.png',
            additionalImage1: '/static/assets/leaves/Kaliyos_1.png',
            additionalImage2: '/static/assets/leaves/Kaliyos_2.png',
            alt: 'Kaliyos Leaf'
        },
        mango: {
            title: 'Mango Leaf',
            content: 'Mangifera indica, commonly known as mango, is a species of lowering plant in the family Anacardiaceae. There are two distinct genetic populations in modern mangoes – the "Indian type" and the "Southeast Asian type". The species was first described by Linnaeus in 1753. Manga is a large tree, with a dense and spreading crown. Leaves are oblong to oblong-lanceolate, 10 to 30 centimeters long. The flowers are yellow, small, 3 to 4 millimeters long, borne on erect and hairy panicles, which as as often as long as the leaves. The fruit is a drupe, of varying shades of yellow, fleshy, oblong-ovoid,10 to 15 centimeters long, and slightly compressed, the skin is thin, and in the center is a large flattened, fibrous seed, and when ripe, surrounded by an edible yellow pulp.',
            mainImage: '/static/assets/leaves/mango.png',
            additionalImage1: '/static/assets/leaves/Mango_1.png',
            additionalImage2: '/static/assets/leaves/Mango_2.png',
            alt: 'Mango Leaf'
        },
        mulawin: {
            title: 'Mulawin Leaf',
            content: ' Vitex pinnata is a species of tree in the family Lamiaceae.- The name "molave" is Spanish, derived from mulawin, the Tagalog word for the tree.- In the confusing landscape of commom names, "molave" is shared by Vitex parviflora (Mulawin, small-flower chaste tree) and Viitex pinnata (hairy-leafed molave). Both species are native to the Philippines. Molave is a tree that reaches a height of 8 to 15 meters, smooth or nearly so, with inflorescences that may be slightly hairy. Leaflets are three, stalked, ovate to lanceolate, 7 to 18 centimeters long, pointed at the tip, shining and quite smooth. Flowers are blue, numerous, 6 to 8 millimeters long, hairy outside the corolla, borne on terminal, paniculate and ample inflorescences, up to 20 centimeters in length. Fruit is rounded, 5 to 6 millimeters in diameter.',
            mainImage: '/static/assets/leaves/mulawin.png',
            additionalImage1: '/static/assets/leaves/Mulawin_1.png',
            additionalImage2: '/static/assets/leaves/Mulawin_2.png',
            alt: 'Mulawin Leaf'
        },
        'palawan-cherry': {
            title: 'Palawan Cherry Leaf',
            content: ' The Balayong Tree, also known as the “Palawan Cherry Tree”, is native to Puerto Princesa. While it resembles the Sakura tree in appearance, is it actually closer in species to other local trees like the Acacia and the Narra.  It is a small to medium-sized tree that can grow to a height of 15 meters or taller. bloom between March and April. Expected to be fully grown in 5 years. Balayong are usually low maintenance, but the young plants require extra phosphorus to encourage good root development. Good for soil stabilization. The Palawan Cherry is being grown as an ornamental plant. And it is used for cultivation purposes',
            mainImage: '/static/assets/leaves/palawan_cherry.png',
            additionalImage1: '/static/assets/leaves/Palawan_1.png',
            additionalImage2: '/static/assets/leaves/Palawan_2.png',
            alt: 'Palawan Cherry Leaf'
        },
        'ylang-ylang': {
            title: 'Ylang-Ylang Leaf',
            content: 'Cananga is a small genus of trees in the family Annonaceae. Ylang-ylang is the Spanish spelling of its Tagalog name, ilang-ilang, a reduplicative form of the word "ilang", meaning "wilderness", alluding to the trees natural habitat. A common mistranslation is flower of flowers. Ilang-ilang is a medium-sized tree growing 10 to 30 meters in height, with pendulous branches, with drooping, leafy twigs. Flowers are fragrant, axillary, in umbellate hanging clusters, with three sepals and six petals, twisted when young and drooping when mature. Leaves are dark green, up to 20 centimeters in length, alternate, simple, entire. Fruit is black in color, 1.5 to 2 centimeters in length, in axillary clusters, fleshy and olive-like, with six to 12 seeds in each fruit.',
            mainImage: '/static/assets/leaves/ylang-ylang.png',
            additionalImage1: '/static/assets/leaves/Ylang_1.png',
            additionalImage2: '/static/assets/leaves/Ylang_2.png',
            alt: 'Ylang-Ylang Leaf'
        }
    };

    function createLeafPopup(leafName) {
        const leaf = leafData[leafName];
        const popup = document.createElement('div');
        popup.classList.add('popup-overlay', 'leaf-popup');
        popup.innerHTML = `
            <div class="popup-container">
                <button class="close-btn">&times;</button>
                <div class="images-container">
                    <img src="${leaf.mainImage}" alt="${leaf.alt}">
                    <img src="${leaf.additionalImage1}" alt="${leaf.alt}">
                    <img src="${leaf.additionalImage2}" alt="${leaf.alt}">
                </div>
                <h2>${leaf.title}</h2>
                <p>${leaf.content}</p>
            </div>
        `;
        leafPopups.appendChild(popup);

        const closeBtn = popup.querySelector('.close-btn');
        closeBtn.addEventListener('click', function() {
            popup.remove();
        });

        popup.style.display = 'flex';
    }

    const boxes = document.querySelectorAll('.box');

    boxes.forEach(box => {
        box.addEventListener('click', function() {
            const leafName = this.dataset.leaf;
            createLeafPopup(leafName);
        });
    });

    const backToTopButton = document.getElementById("backToTop");

    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        const homeSection = document.getElementById("logo");
        const homeSectionHeight = homeSection.offsetHeight;

        if (document.body.scrollTop > homeSectionHeight || document.documentElement.scrollTop > homeSectionHeight) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    }

    backToTopButton.onclick = function() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    };

    const searchInput = document.getElementById('search');

    searchInput.addEventListener('input', function() {
        const searchValue = searchInput.value.toLowerCase();
        boxes.forEach(box => {
            const text = box.textContent.toLowerCase();
            if (text.includes(searchValue)) {
                box.style.display = 'flex';
            } else {
                box.style.display = 'none';
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const uploadInput = document.getElementById('upload');
    const uploadImagePreview = document.getElementById('upload-image-preview');
    const cancelBtn = document.querySelector('.cancel-btn');
    const defaultImageSrc = uploadImagePreview.getAttribute('data-default-src');  // Get the default image source from data attribute

    uploadInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                uploadImagePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    cancelBtn.addEventListener('click', function() {
        uploadInput.value = "";  // Clear the file input
        uploadImagePreview.src = defaultImageSrc;  // Reset the preview image to the default image
    });
});

// Disable pinch zoom gesture on touch-enabled devices
document.addEventListener('touchmove', function(event) {
    if (event.scale !== 1) { event.preventDefault(); }
}, { passive: false });

// Disable zoom functionality on desktop browsers
window.addEventListener('wheel', function(event) {
    if (event.ctrlKey) { event.preventDefault(); }
}, { passive: false });

// Disable zooming using ctrl key and +/- keys
window.addEventListener('keydown', function(e) {
    if (e.ctrlKey && (e.key === '+' || e.key === '-' || e.key === '=')) {
        e.preventDefault();
    }
});
