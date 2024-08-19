#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndustryPetArchiveDTO import IndustryPetArchiveDTO


class AlipayCommercePetMerchantarchiveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetMerchantarchiveQueryResponse, self).__init__()
        self._pet_archive_info = None

    @property
    def pet_archive_info(self):
        return self._pet_archive_info

    @pet_archive_info.setter
    def pet_archive_info(self, value):
        if isinstance(value, IndustryPetArchiveDTO):
            self._pet_archive_info = value
        else:
            self._pet_archive_info = IndustryPetArchiveDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetMerchantarchiveQueryResponse, self).parse_response_content(response_content)
        if 'pet_archive_info' in response:
            self.pet_archive_info = response['pet_archive_info']
