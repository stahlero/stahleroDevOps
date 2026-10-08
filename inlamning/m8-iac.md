M8 – Terraform iaC

Jag använde terraform för att skapa samma miljö som i M7 i cpouta.

Terraform skapade 8 resurser och gav Floating ip adressen 86.50.20.208. Jag testade appen externt och den fungerade via både floating ip och nip.io.

Jag tog bort den gamla M7-VM:n och dens Floating ip efter att terraform miljön fungerade.

terraform state list visade 9 poster, inklusive terraform-resurserna och nätverkets data source.

Jag testade även att ta bort terraform VM:n med terraform destroy -target="openstack_compute_instance_v2.this" och körde sedan terraform apply igen. vm:n skapades på nytt och samma floating ip 86.50.20.208 användes igen.


Terraform apply med 8 nya resurser
Appen fungerande via Floating ip och nip.io
M7 vm:n och gamla floating ip:n borttagna
terraform state list med 9 poster
Rebuild av VM:n med samma floating ip
