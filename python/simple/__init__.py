class RSUEducationAPIView:

    # Adam's
    def get_object(self):
        rsu_pks = list(
                RSU.objects
                .filter(
                    owner_id=self.portfolio_pk,
                    corporation_id=self.entity_pk,
                    so_type=SO_TYPE_RSU,
                )
                .annotate_vested_shares()
                .filter(vested_shares=Decimal(0))
                .values_list('pk', flat=True)
            )

    # Jair and Brett
    def get_object(self):
        # RSU - Model...    ActiveRecord
        # RSU.objects       ModelManager
        # RSU.objects.all() QuerySet

        # pk's is your responsiblity

        rsu_pks = list(
            RSU.objects.
                # .filter(so_type=SO_TYPE_RSU)
                .for_owner(self.portfolio_pk)
                .for_corporation(self.entity_pk)
                .unvested()
                .values_list('pk', flat=True)
            )
