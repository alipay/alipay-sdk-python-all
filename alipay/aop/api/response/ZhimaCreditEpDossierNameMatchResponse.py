#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpDossierLiteDetail import EpDossierLiteDetail


class ZhimaCreditEpDossierNameMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierNameMatchResponse, self).__init__()
        self._ep_dossier_lite_detail = None

    @property
    def ep_dossier_lite_detail(self):
        return self._ep_dossier_lite_detail

    @ep_dossier_lite_detail.setter
    def ep_dossier_lite_detail(self, value):
        if isinstance(value, list):
            self._ep_dossier_lite_detail = list()
            for i in value:
                if isinstance(i, EpDossierLiteDetail):
                    self._ep_dossier_lite_detail.append(i)
                else:
                    self._ep_dossier_lite_detail.append(EpDossierLiteDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierNameMatchResponse, self).parse_response_content(response_content)
        if 'ep_dossier_lite_detail' in response:
            self.ep_dossier_lite_detail = response['ep_dossier_lite_detail']
