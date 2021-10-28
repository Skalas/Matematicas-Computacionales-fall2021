(require 'package)

(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("melpa-stable" . "https://stable.melpa.org/packages/")
                         ("org" . "https://orgmode.org/elpa/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))
(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

(unless (package-installed-p 'use-package)
  (package-install 'use-package))
(require 'use-package)
(setq use-package-always-ensure t)
(setq use-package-always-defer t)

(defun skls/insert-r-pipe ()
  "R - %>% operator or 'then' pipe operator"
  (interactive)
  (just-one-space 1)
  (insert "%>%")
  (reindent-then-newline-and-indent))

(use-package ess
  :commands R
  :bind (
         :map ess-mode-map
              ("C-<" . ess-insert-assign)
              ("C->" . skls/insert-r-pipe)
              :map inferior-ess-mode-map
              ("C-<" . ess-insert-assign)
              ("C->" . skls/insert-r-pipe)
              )
  :init
  (load "ess-r-mode")
  )
