(function () {
  "use strict";

  var modal = document.getElementById("edit-modal");
  var fileInput = document.getElementById("id_profile_picture");
  var avatarPreview = document.getElementById("avatar-preview");
  var fileName = document.getElementById("file-name");
  var toastBox = document.getElementById("toasts");

  function showToast(text) {
    var box = toastBox;
    if (!box) {
      box = document.createElement("div");
      box.className = "toasts";
      box.id = "toasts";
      document.body.appendChild(box);
    }
    var toast = document.createElement("div");
    toast.className = "toast";
    toast.textContent = text;
    var close = document.createElement("button");
    close.className = "x";
    close.type = "button";
    close.setAttribute("aria-label", "Dismiss");
    close.innerHTML = "&times;";
    toast.appendChild(close);
    box.appendChild(toast);
    setTimeout(function () {
      toast.classList.add("out");
      setTimeout(function () { toast.remove(); }, 250);
    }, 4000);
  }

  function openModal() {
    modal.classList.add("open");
    document.body.classList.add("locked");
  }

  function closeModal() {
    modal.classList.remove("open");
    document.body.classList.remove("locked");
  }

  document.addEventListener("click", function (event) {
    if (event.target.closest('[data-open="edit-modal"]')) {
      openModal();
      return;
    }
    if (event.target.closest("[data-close]")) {
      closeModal();
      return;
    }
    var inert = event.target.closest("[data-inert]");
    if (inert) {
      showToast(inert.getAttribute("data-inert"));
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && modal.classList.contains("open")) {
      closeModal();
    }
  });

  if (fileInput) {
    fileInput.addEventListener("change", function () {
      var file = fileInput.files && fileInput.files[0];
      if (!file) return;
      fileName.textContent =
        file.name + " (" + Math.round(file.size / 1024) + " KB)";
      var reader = new FileReader();
      reader.onload = function () {
        avatarPreview.textContent = "";
        var img = document.createElement("img");
        img.src = reader.result;
        img.alt = "New profile picture preview";
        avatarPreview.appendChild(img);
      };
      reader.readAsDataURL(file);
    });
  }

  var tabs = document.querySelectorAll(".tabs a");
  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      tabs.forEach(function (other) { other.classList.remove("on"); });
      tab.classList.add("on");
    });
  });

  document.querySelectorAll("[data-like]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      btn.classList.toggle("liked");
    });
  });

  if (toastBox) {
    toastBox.addEventListener("click", function (event) {
      var toast = event.target.closest(".toast");
      if (toast) toast.remove();
    });
    toastBox.querySelectorAll(".toast").forEach(function (toast) {
      setTimeout(function () {
        toast.classList.add("out");
        setTimeout(function () { toast.remove(); }, 250);
      }, 4000);
    });
  }
})();
