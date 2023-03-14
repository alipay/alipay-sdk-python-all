#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ImportSignerInfo import ImportSignerInfo


class AlipayBossProdAntlegalchainNdasignerCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainNdasignerCreateResponse, self).__init__()
        self._import_signer_info_list = None

    @property
    def import_signer_info_list(self):
        return self._import_signer_info_list

    @import_signer_info_list.setter
    def import_signer_info_list(self, value):
        if isinstance(value, list):
            self._import_signer_info_list = list()
            for i in value:
                if isinstance(i, ImportSignerInfo):
                    self._import_signer_info_list.append(i)
                else:
                    self._import_signer_info_list.append(ImportSignerInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainNdasignerCreateResponse, self).parse_response_content(response_content)
        if 'import_signer_info_list' in response:
            self.import_signer_info_list = response['import_signer_info_list']
