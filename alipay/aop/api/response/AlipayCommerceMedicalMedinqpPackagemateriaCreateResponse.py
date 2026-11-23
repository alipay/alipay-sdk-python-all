#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedinqpPackagemateriaCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedinqpPackagemateriaCreateResponse, self).__init__()
        self._back_poster_url = None
        self._materia_content = None
        self._poster_url = None
        self._qr_image_url = None
        self._redirect_url = None

    @property
    def back_poster_url(self):
        return self._back_poster_url

    @back_poster_url.setter
    def back_poster_url(self, value):
        self._back_poster_url = value
    @property
    def materia_content(self):
        return self._materia_content

    @materia_content.setter
    def materia_content(self, value):
        self._materia_content = value
    @property
    def poster_url(self):
        return self._poster_url

    @poster_url.setter
    def poster_url(self, value):
        self._poster_url = value
    @property
    def qr_image_url(self):
        return self._qr_image_url

    @qr_image_url.setter
    def qr_image_url(self, value):
        self._qr_image_url = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedinqpPackagemateriaCreateResponse, self).parse_response_content(response_content)
        if 'back_poster_url' in response:
            self.back_poster_url = response['back_poster_url']
        if 'materia_content' in response:
            self.materia_content = response['materia_content']
        if 'poster_url' in response:
            self.poster_url = response['poster_url']
        if 'qr_image_url' in response:
            self.qr_image_url = response['qr_image_url']
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
