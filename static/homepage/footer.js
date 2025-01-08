document.addEventListener("DOMContentLoaded", function () {
    const footerSections = [
        {
            title: "Useful Links",
            links: [
                { label: "About", link: "#about" },
                { label: "Careers", link: "#careers" },
                { label: "Blog", link: "#blog" },
                { label: "Press", link: "#press" },
                { label: "Lead", link: "#lead" },
                { label: "Value", link: "#value" },
                { label: "Privacy", link: "#privacy" },
                { label: "Terms", link: "#terms" },
                { label: "FAQs", link: "#faqs" },
                { label: "Security", link: "#security" },
                { label: "Mobile", link: "#mobile" },
                { label: "Contact", link: "#contact" }
            ]
        },
        {
            title: "Categories",
            links: [
                { label: "Vegetables & Fruits", link: "#vegetables-fruits" },
                { label: "Dairy & Breakfast", link: "#dairy-breakfast" },
                { label: "Instant & Frozen Food", link: "#instant-frozen" },
                { label: "Snacks", link: "#snacks" },
                { label: "Beverages", link: "#beverages" },
                { label: "Paan Corner", link: "#paan-corner" }
            ]
        }
    ];

    const footer = document.createElement("footer");
    footer.className = "bg-white p-6 mt-8 text-gray-700";

    let content = '<div class="container mx-auto"><div class="grid grid-cols-1 md:grid-cols-3 gap-8">';

    footerSections.forEach(section => {
        content += `<div><h3 class="font-bold mb-2">${section.title}</h3><ul class="space-y-1">`;
        section.links.forEach(item => {
            content += `<li><a href="${item.link}" class="hover:text-blinkit-green">${item.label}</a></li>`;
        });
        content += '</ul></div>';
    });

    content += `
        <div class="text-right">
            <p class="mb-2">&copy; Blink Commerce Private Limited, 2016-2025</p>
            <p class="mb-2">Download App:</p>
            <div class="flex justify-end space-x-2">
                <button class="border border-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-100 transition duration-300">App Store</button>
                <button class="border border-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-100 transition duration-300">Google Play</button>
            </div>
        </div>
    </div></div>`;

    footer.innerHTML = content;
    document.body.appendChild(footer);
});
